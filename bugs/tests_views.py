from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Bugs
from django.contrib.auth.models import User
from .forms import BugsPostForm

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "base.html")
        
    def test_get_add_bug_page(self):
        User.objects.create_user(
            username='TestBugPost1',
            email='TestBug1@example.com',
            password='password1')

        bug = Bugs.objects.create(title='Test Bug Post',
                                   content='Test Bug Post Content')

        self.assertEqual(bug.content, 'Test Bug Post Content')

        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

        bug.content = 'Test bug Post Edit Content'
        bug.save()

        self.assertEqual(bug.title, 'Test Bug Post')
        self.assertEqual(bug.content, 'Test bug Post Edit Content')

        response = self.client.get('/bugs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bugs.html")
    
    def test_get_edit_bug_page(self):
        User.objects.create_user(
            username='TestBug1',
            email='TestBugPost1@example.com',
            password='password1')
        self.client.login(username='TestBugPost1', password='password1')

        bug = Bugs.objects.create(title='Test Bug Post',
                                   content='Test Bug Content')

        page = self.client.get('/bugs/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

        bug.content = 'Test Bug Content'
        bug.save()

        self.assertEqual(bug.content,
                         'Test Bug Content')
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/1")
        self.assertEqual(page.status_code, 404)    
        
#    def test_upvote_bug(self):
#        admin = User(username="admin")
#        admin.save()
#        bug = Bugs(title="test", content="test")
#        bug.save()
#        
#        page = self.client.post("/bug/upvote{0}/".format(bug.id))
#        bug.refresh_from_db()
#        self.assertEqual(page.status_code, 302)
#        self.assertEqual(bug.upvotes, 1)