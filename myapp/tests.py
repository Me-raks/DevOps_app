from django.test import TestCase

from django.urls import reverse
from .models import CustomUser

class URLTests(TestCase):
    def test_homepage(self):
        response= self.client.get('http://127.0.0.1:8000/users/')
        self.assertEqual(response.status_code, 200)

class UserListViewTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', email='test@example.com', first_name='John', last_name='Doe')
        self.url = reverse('user-list')

    def test_user_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'test@example.com')


class CountVisitsViewTestCase(TestCase):
    def test_count_visits_view(self):
        url = reverse('count-visits')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['visit_count'], 1)

        # Test for multiple visits
        response = self.client.get(url)
        self.assertEqual(response.json()['visit_count'], 2)