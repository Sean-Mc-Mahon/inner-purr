from django.test import TestCase
from .models import Product


class TestViews(TestCase):

    def test_get_all_products_view(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_details_view(self):
        product = Product.objects.create(name='buttons', description='pins', price=2.99)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')