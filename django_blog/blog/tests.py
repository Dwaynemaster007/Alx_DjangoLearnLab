from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Comment, Post


class BlogFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='writer', password='Str0ng-pass!')
        self.other = User.objects.create_user(username='reader', password='Str0ng-pass!')
        self.post = Post.objects.create(title='Hello Eswatini', content='First post body', author=self.user)

    def test_public_pages(self):
        for url in [reverse('post_list'), reverse('post_detail', args=[self.post.pk]), reverse('login'),
                    reverse('register'), reverse('search') + '?q=Hello', reverse('search')]:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, url)
        self.assertContains(self.client.get(reverse('post_list')), 'Hello Eswatini')
        self.assertContains(self.client.get(reverse('search') + '?q=Eswatini'), 'Hello Eswatini')

    def test_register_and_login(self):
        response = self.client.post(reverse('register'), {
            'username': 'newbie', 'email': 'newbie@example.com',
            'password1': 'An0ther-pass!', 'password2': 'An0ther-pass!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newbie').exists())
        self.assertTrue(self.client.login(username='newbie', password='An0ther-pass!'))
        self.assertEqual(self.client.get(reverse('profile')).status_code, 200)

    def test_post_crud_and_permissions(self):
        self.assertEqual(self.client.get(reverse('post_create')).status_code, 302)  # must log in
        self.client.login(username='writer', password='Str0ng-pass!')
        response = self.client.post(reverse('post_create'), {'title': 'Second', 'content': 'More words', 'tags': 'django, python'})
        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(title='Second')
        self.assertEqual(self.client.get(reverse('tagged_posts', args=['django'])).status_code, 200)

        response = self.client.post(reverse('post-update', args=[post.pk]), {'title': 'Second (edited)', 'content': 'More words', 'tags': 'django'})
        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Second (edited)')

        self.client.logout()
        self.client.login(username='reader', password='Str0ng-pass!')
        self.assertEqual(self.client.post(reverse('post_delete', args=[post.pk])).status_code, 403)

        self.client.logout()
        self.client.login(username='writer', password='Str0ng-pass!')
        self.assertEqual(self.client.post(reverse('post_delete', args=[post.pk])).status_code, 302)
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())

    def test_comments(self):
        self.client.login(username='reader', password='Str0ng-pass!')
        response = self.client.post(reverse('comment-create', args=[self.post.pk]), {'content': 'Great read!'})
        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.get(content='Great read!')
        self.assertContains(self.client.get(reverse('post_detail', args=[self.post.pk])), 'Great read!')
        response = self.client.post(reverse('comment-update', args=[comment.pk]), {'content': 'Great read, thanks!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.post(reverse('comment-delete', args=[comment.pk])).status_code, 302)
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())
