from django.test import TestCase
from .forms import OrderForm
from django_countries.fields import CountryField


class TestOrderForm(TestCase):

    def test_item_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0],
            'This field is required.')

    def test_fields_are_explicit_in_form_meta_class(self):
        form = OrderForm()
        self.assertEqual(
            form.Meta.fields,
            ('full_name',
             'email',
             'phone_number',
             'street_address1',
             'street_address2',
             'town_or_city',
             'postcode',
             'country',
             'county'))
