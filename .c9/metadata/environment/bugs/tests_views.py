{"filter":false,"title":"tests_views.py","tooltip":"/bugs/tests_views.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":26,"column":51},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":27,"column":0},"end":{"row":27,"column":8},"action":"insert","lines":["        "]},{"start":{"row":27,"column":8},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":28,"column":4},"end":{"row":31,"column":42},"action":"insert","lines":["    def test_post_create_an_bug(self):","        response = self.client.post(\"/new_bug\", {\"title\": \"Create a Test\"})","        bug = get_object_or_404(Bugs, pk=1)","        self.assertEqual(bug.done, False) "],"id":3}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":8},"action":"remove","lines":["    "],"id":4}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":61},"action":"remove","lines":["from .views import get_bugs, bugs_detail, create_or_edit_bug "],"id":5}],[{"start":{"row":0,"column":32},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":6}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":46},"action":"insert","lines":["from django.shortcuts import get_object_or_404"],"id":7}],[{"start":{"row":29,"column":0},"end":{"row":32,"column":43},"action":"remove","lines":["    def test_post_create_an_bug(self):","        response = self.client.post(\"/new_bug\", {\"title\": \"Create a Test\"})","        bug = get_object_or_404(Bugs, pk=1)","        self.assertEqual(bug.done, False)  "],"id":8}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":26},"action":"remove","lines":["class TestViews(TestCase):"],"id":16},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]},{"start":{"row":5,"column":26},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":14,"column":50},"action":"insert","lines":["class TestViews(TestCase):","    def setUp(self):","        user = User.objects.create_user(username='username', password='password')","        self.client.login(username='username', password='password')","    def test_get_bugs_page(self):","        page = self.client.get(\"/bugs/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"bugs.html\")"],"id":15}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["#"],"id":13}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["#"],"id":12}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["#"],"id":11}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"insert","lines":["#"],"id":10}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["#"],"id":9}]]},"ace":{"folds":[],"scrolltop":1.5,"scrollleft":0,"selection":{"start":{"row":11,"column":0},"end":{"row":11,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565650897939,"hash":"2c74af7f73bad66c69afcf64ac6e0826949903e0"}