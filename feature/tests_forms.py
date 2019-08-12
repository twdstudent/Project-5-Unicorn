from django.test import TestCase
from .forms import FeaturesPostForm

class TestFeaturesPostForm(TestCase):

    def test_can_create_an_feature_with_just_a_title_and_content(self):
        form = FeaturesPostForm({
            'title': 'Feature Title',
            'content': 'Lorm Ipsum',
            
        })
        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_missing_title(self):
        form = FeaturesPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])