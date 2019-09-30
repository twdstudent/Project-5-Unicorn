from django.test import TestCase
from .forms import BugsPostForm

class TestBugForm(TestCase):
    
    def test_bug_content(self):
        form = BugsPostForm({'Title': 'Title'})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])
        
    def test_cannot_create_a_bug_with_required_values(self):
        form = BugsPostForm({'title': "Test"})
        self.assertFalse(form.is_valid())