from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User

# testing login and registration forms.

class TestAccountsForms(TestCase):
    def test_login_password_required(self):
        form = UserLoginForm({'username': 'admin'})
        self.assertFalse(form.is_valid())
        print(form.errors['password'], ['This field is required.'])

    def test_login_username_required(self):
        form = UserLoginForm({'password': 'T-DOG'})
        self.assertFalse(form.is_valid())
        print(form.errors['username'], ['This field is required.'])

    def test_registration_passwords_must_match(self):
        form = UserRegistrationForm({
            'email': 'admin@example.com',
            'username': 'admin',
            'password1': 'pa55word1',
            'password2': 'pa55word2'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ["The two password fields didn't match."])

    def test_login_form(self):
            form = UserLoginForm({
                'username': 'admin',
                'password': 'pa55word'
            })
            self.assertTrue(form.is_valid())
            
    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username='testuser',
            email='admin@example.com')

        form = UserRegistrationForm({
            'email': 'admin@example.com',
            'username': 'admin',
            'password1': 'pa55word1',
            'password2': 'pa55word1'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],
                         ['Email address must be unique'])        