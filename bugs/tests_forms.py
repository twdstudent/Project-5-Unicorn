from django.test import TestCase
from .forms import BugsPostForm

class TestBugsPostForm(TestCase):

    def test_can_create_an_bug_with_just_a_name(self):
        form = BugsPostForm({'name': 'Create Tests'})
        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_missing_name(self):
        form = BugsPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])