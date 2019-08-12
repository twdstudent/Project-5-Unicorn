from django.test import TestCase
from .models import Feature

# Create your tests here.
class FeatureTests(TestCase):
    """
    Define the tests that we'll run against
    bugs model
    """

    def test_str(self):
        test_title = Feature(title='A feature')
        self.assertEqual(str(test_title), 'A feature')
