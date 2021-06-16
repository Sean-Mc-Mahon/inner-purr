from django.test import TestCase
from .forms import UserProfileForm

class TestUserProfileForm(TestCase):

    def test_item_phone_number_is_not_required(self):
        form = UserProfileForm({'default_phone_number': ''})
        self.assertTrue(form.is_valid())
