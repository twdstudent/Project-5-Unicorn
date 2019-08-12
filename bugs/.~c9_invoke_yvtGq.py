from django.test import TestCase
from .models import Bugs
from .views import get_bugs, bugs_detail, create_or_edit_bug 

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "base.html")
        
#    def test_get_add_bug_page(self):
#        page = self.client.get("/new_bug")
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "bug-post-form.html")    
#    
#    def test_get_edit_item_page(self):
#        bug = Bugs(title="Create a Test")
#        bug.save()
#
#        page = self.client.get("/edit_bug/{0}".format(bug.id))
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "bug-detail.html")
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/1")
        self.assertEqual(page.status_code, 404)    
        
    def test_post_create_an_bug(self):
        response = self.client.post("/new_bug", {"title": "Create a Test"})
        bug = get_object_or_404(Bugs, pk=1)
        self.assertEqual(bug.done, False)     