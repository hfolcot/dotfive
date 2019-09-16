from django.contrib.auth.models import User
from django.test import TestCase, Client


from .models import Category

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create(username='test')
        user.set_password('testing321')
        user.save()

    def test_get_home_page_unauthenticated(self):
        #App should redirect user to the login page
        page = self.client.get('/')
        self.assertRedirects(page, '/accounts/login?next=/')

    def test_get_home_page_authenticated(self):
        #App should open home page with the categories.html template when user authenticated
        self.client.login(username='test', password='testing321')
        page = self.client.get('/', follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'categories.html')