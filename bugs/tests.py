from django.test import TestCase
from .models import Bugs

# Create your tests here.
class BugTests(TestCase):
    """
    Define the tests that we'll run against
    bugs model
    """

    def test_str(self):
        test_title = Bugs(title='A bug')
        self.assertEqual(str(test_title), 'A bug')
