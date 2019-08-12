from django.test import TestCase
from .forms import BugsPostForm

class TestBugsPostForm(TestCase):

    def test_can_create_an_bug_with_just_a_title(self):
        form = BugsPostForm({
            'title': 'Bug Title',
            'content': 'Lorm Ipsum',
            
        })
        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_missing_title(self):
        form = BugsPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])