from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.checkout = reverse("checkout")
    
    def test_checkout_view(self):
        response = self.client.get(self.checkout)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'checkout/checkout.html')