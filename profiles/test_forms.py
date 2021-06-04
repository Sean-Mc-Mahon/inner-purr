from django.test import TestCase
from .forms import UserProfileForm

class TestUserProfileForm(TestCase):

    def test_item_name_is_required(self):
        form = UserProfileForm({'default_phone_number': '25246553'},{'default_postcode': 'Postal Code'},{'default_town_or_city': 'town'},{'default_street_address1': 'street'},{'default_street_address2': 'street2'},{'default_county': 'county'})
        self.assertFalse(form.is_valid())
        self.assertIn('default_phone_number', form.errors.keys())
        self.assertEqual(form.errors['default_phone_number'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = UserProfileForm({'default_phone_number': '25246553'},{'default_postcode': 'Postal Code'},{'default_town_or_city': 'town'},{'default_street_address1': 'street'},{'default_street_address2': 'street2'},{'default_county': 'county'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.fields, ['order_number', 'user_profile', ''])
