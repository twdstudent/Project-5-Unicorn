from django.test import TestCase
from .models import Feature

class TestItemModel(TestCase):

    def test_done_defaults_to_False(self):
        feature = Feature(title="Create a Test")
        feature.save()
        self.assertEqual(feature.title, "Create a Test")
        self.assertFalse(feature.content)
    
    def test_can_create_an_feature_with_a_name_and_content(self):
        feature = Feature(title="Create a Test", content="Lorem Ipsum")
        feature.save()
        self.assertEqual(feature.title, "Create a Test")
        self.assertTrue(feature.content)