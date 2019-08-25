from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Feature
from django.contrib.auth.models import User
from .forms import FeaturesPostForm

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "base.html")
        
    def test_get_add_feature_page(self):
        User.objects.create_user(
            username='TestBugPost1',
            email='TestBug1@example.com',
            password='password1')

        feature = Feature.objects.create(title='Test Feature Post',
                                   content='Test Feature Post Content')

        self.assertEqual(feature.content, 'Test Feature Post Content')

        page = self.client.get("/feature/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature.html")

        feature.content = 'Test Feature Post Edit Content'
        feature.save()

        self.assertEqual(feature.title, 'Test Feature Post')
        self.assertEqual(feature.content, 'Test Feature Post Edit Content')

        response = self.client.get('/feature/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "feature.html")
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/1")
        self.assertEqual(page.status_code, 404)  
        
   