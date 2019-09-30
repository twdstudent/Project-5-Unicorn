from django.test import TestCase
from .forms import FeaturesPostForm

class TestFeatureForm(TestCase):
    
    def test_feature_content(self):
        form = FeaturesPostForm({'Title': 'Title'})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])
        
    def test_cannot_create_a_feature_with_required_values(self):
        form = FeaturesPostForm({'title': 'Test'})
        self.assertFalse(form.is_valid())