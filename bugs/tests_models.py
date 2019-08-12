from django.test import TestCase
from .models import Bugs


class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        bug = Bugs(title="Create a Test")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertFalse(bug.content)
    
    def test_can_create_an_bug_with_a_name_and_content(self):
        bug = Bugs(title="Create a Test", content="Lorem Ipsum")
        bug.save()
        self.assertEqual(bug.title, "Create a Test")
        self.assertTrue(bug.content)