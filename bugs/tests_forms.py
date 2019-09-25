from django.test import TestCase
from .forms import BugsPostForm

#class TestBugsPostForm(TestCase):
#
#    def test_can_create_an_bug_with_requirede_features(self):
#        form = BugsPostForm({
#            'title': 'test bug',
#            'content': 'bug content',
#            'status': 'todo',
#            'owner': 'test owner'
#        })
#        self.assertTrue(form.is_valid())
   
#    def test_correct_message_for_missing_title(self):
#       form = BugsPostForm({'form': ''})
#        self.assertFalse(form.is_valid())
#        self.assertEqual(form.errors['title'], ['This field is required.'])