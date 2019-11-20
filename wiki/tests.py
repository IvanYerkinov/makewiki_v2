from django.test import TestCase
from wiki.models import Page
from django.contrib.auth.models import User


# Create your tests here.
class WikiTestCase(TestCase):
    def test_true(self):
        self.assertEqual(True, True)

    def test_get(self):
        response = self.client.get('/new/')
        self.assertEqual(response.status_code, 200)

    def test_creation_page(self):

        user = User.objects.create()

        dict = {'title': "TEST", 'author': 1, 'content': 'test'}

        response = self.client.post('/new/', dict)

        self.assertEqual(response.status_code, 200)

        slug = Page.objects.get(title="TEST").slug

        response = self.client.get('/' + slug + '/')

        self.assertEqual(response.status_code, 200)

    def test_slug_page(self):
        user = User.objects.create()
        Page.objects.create(title="TEST CONTENT", content="test", author=user)
        slug = Page.objects.get(title="TEST CONTENT").slug

        response = self.client.get('/' + slug + '/')

        self.assertEqual(response.status_code, 200)
