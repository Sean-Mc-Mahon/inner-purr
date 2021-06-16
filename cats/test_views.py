from django.test import TestCase, Client
from .models import Cat
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.cats = reverse("cats")

    def test_get_all_cats_view(self):
        response = self.client.get(self.cats)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cats/cats.html')

    def test_get_cat_details_view(self):
        cat = Cat.objects.create(name='buttons', age='2 years', status='adopted')
        response = self.client.get(f'/cats/{cat.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cats/cat_detail.html')