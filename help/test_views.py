from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.help = reverse("help")

    def test_response_200(self):
        response = self.client.get(self.help)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'help/help.html')
