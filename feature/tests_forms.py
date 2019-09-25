from django.test import TestCase
from .forms import FeaturesPostForm

#class TestFeaturesPostForm(TestCase):

#    def test_can_create_an_feature_with_required_values(self):
#        form = FeaturesPostForm({
#            'title': 'Feature Title',
#            'content': 'Lorm Ipsum',
#            'status': 'todo',
#            'owner': 'newby',
#        })
#        self.assertTrue(form.is_valid())
        
#    def test_correct_message_for_missing_title(self):
#        form = FeaturesPostForm({'form': ''})
#        self.assertTrue(form.is_valid())
#        self.assertEqual(form.errors['title'], ['This field is required.'])