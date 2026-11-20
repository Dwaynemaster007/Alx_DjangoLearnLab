from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from .models import Author, Book, UserProfile


class LibraryFlowTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Chinua Achebe')
        self.book = Book.objects.create(title='Things Fall Apart', author=self.author, publication_year=1958)
        self.user = get_user_model().objects.create_user(email='reader@example.com', username='reader', password='S3cure-pass!')

    def test_new_users_get_a_member_profile(self):
        self.assertEqual(UserProfile.objects.get(user=self.user).role, 'Member')

    def test_book_list_is_public(self):
        response = self.client.get(reverse('list_books'))
        self.assertContains(response, 'Things Fall Apart')

    def test_register_logs_in_and_shows_books(self):
        response = self.client.post(reverse('register'), {
            'email': 'newbie@example.com', 'username': 'newbie',
            'password1': 'An0ther-pass!', 'password2': 'An0ther-pass!',
        }, follow=True)
        self.assertContains(response, 'Signed in as newbie')

    def test_role_pages(self):
        self.client.login(email='reader@example.com', password='S3cure-pass!')
        self.assertEqual(self.client.get(reverse('member_view')).status_code, 200)
        self.assertEqual(self.client.get(reverse('admin_view')).status_code, 302)

    def test_add_edit_delete_need_permissions(self):
        self.client.login(email='reader@example.com', password='S3cure-pass!')
        self.assertEqual(self.client.get(reverse('add_book')).status_code, 403)
        codenames = ['can_add_book', 'can_change_book', 'can_delete_book']
        self.user.user_permissions.add(*Permission.objects.filter(codename__in=codenames))
        self.client.login(email='reader@example.com', password='S3cure-pass!')

        response = self.client.post(reverse('add_book'), {
            'title': 'Arrow of God', 'author': 'Chinua Achebe', 'publication_year': '1964',
        })
        self.assertRedirects(response, reverse('list_books'))
        new_book = Book.objects.get(title='Arrow of God')
        self.assertEqual(new_book.author, self.author)

        response = self.client.post(reverse('edit_book', args=[new_book.id]), {
            'title': 'Arrow of God (2nd ed.)', 'author': 'Chinua Achebe', 'publication_year': '1974',
        })
        self.assertRedirects(response, reverse('list_books'))
        new_book.refresh_from_db()
        self.assertEqual(new_book.publication_year, 1974)

        response = self.client.post(reverse('delete_book', args=[new_book.id]))
        self.assertRedirects(response, reverse('list_books'))
        self.assertFalse(Book.objects.filter(id=new_book.id).exists())

    def test_auth_pages_render(self):
        for name in ('login', 'register'):
            self.assertEqual(self.client.get(reverse(name)).status_code, 200, name)

    def test_logout(self):
        self.client.login(email='reader@example.com', password='S3cure-pass!')
        response = self.client.post(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
