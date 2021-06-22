from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile = reverse("profile")

    def test_user_profile_view(self):
        response = self.client.get(self.profile)
        self.assertEqual(response.status_code, 302)
