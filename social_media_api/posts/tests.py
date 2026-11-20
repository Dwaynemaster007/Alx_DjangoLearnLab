from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from notifications.models import Notification

from .models import Post


class SocialFlowTests(APITestCase):
    def register(self, username):
        response = self.client.post('/api/accounts/register/', {
            'username': username, 'email': f'{username}@example.com', 'password': 'Str0ng-pass!',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        return response.data['token']

    def auth(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

    def test_full_flow(self):
        alice = self.register('alice')
        bob = self.register('bob')

        # login returns the same token
        response = self.client.post('/api/accounts/login/', {'username': 'alice', 'password': 'Str0ng-pass!'}, format='json')
        self.assertEqual(response.data['token'], alice)

        # alice posts, bob follows alice and sees the post in his feed
        self.auth(alice)
        post = self.client.post('/api/posts/posts/', {'title': 'Hello', 'content': 'First post'}, format='json')
        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        post_id = post.data['id']

        self.auth(bob)
        alice_id = get_user_model().objects.get(username='alice').id
        self.assertEqual(self.client.post(f'/api/accounts/follow/{alice_id}/').status_code, 200)
        feed = self.client.get('/api/posts/feed/')
        self.assertEqual([p['title'] for p in feed.data], ['Hello'])

        # bob likes and comments -> alice gets two notifications
        self.assertEqual(self.client.post(f'/api/posts/posts/{post_id}/like/').status_code, 200)
        self.assertEqual(self.client.post(f'/api/posts/posts/{post_id}/like/').status_code, 400)
        comment = self.client.post('/api/posts/comments/', {'post': post_id, 'content': 'Nice!'}, format='json')
        self.assertEqual(comment.status_code, status.HTTP_201_CREATED)

        # bob cannot edit alice's post
        response = self.client.patch(f'/api/posts/posts/{post_id}/', {'title': 'Hacked'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.auth(alice)
        notes = self.client.get('/api/notifications/')
        self.assertEqual(notes.data['count'], 2)
        self.client.post('/api/notifications/mark_as_read/')
        self.assertFalse(Notification.objects.filter(read=False).exists())

        # profile and unfollow
        profile = self.client.get('/api/accounts/profile/')
        self.assertEqual(profile.data['followers_count'], 1)
        self.auth(bob)
        self.client.post(f'/api/accounts/unfollow/{alice_id}/')
        self.assertEqual(self.client.get('/api/posts/feed/').data, [])

    def test_cannot_follow_yourself(self):
        token = self.register('carol')
        self.auth(token)
        me = get_user_model().objects.get(username='carol')
        self.assertEqual(self.client.post(f'/api/accounts/follow/{me.id}/').status_code, 400)

    def test_posts_are_public_but_writing_needs_login(self):
        author = get_user_model().objects.create_user(username='dave', password='Str0ng-pass!')
        Post.objects.create(title='Public', content='Anyone can read', author=author)
        self.assertEqual(self.client.get('/api/posts/posts/').status_code, 200)
        response = self.client.post('/api/posts/posts/', {'title': 'x', 'content': 'y'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
