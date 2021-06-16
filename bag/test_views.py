from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def test_get_all_cats_view(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')