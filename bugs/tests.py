from django.test import TestCase
from .models import Bugs

# Create your tests here.
class ProductTests(TestCase):
    """
    Define the tests that we'll run against
    bugs model
    """

    def test_str(self):
        test_name = Bugs(name='A bug')
        self.assertEqual(str(test_name), 'A bug')
