{"filter":false,"title":"tests_models.py","tooltip":"/feature/tests_models.py","undoManager":{"mark":28,"position":28,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":24},"action":"insert","lines":["from django.test import TestCase","from .models import Bugs"],"id":1}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["s"],"id":2},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"remove","lines":["g"]},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"remove","lines":["u"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"remove","lines":["B"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["F"],"id":3},{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["e"]},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["a"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["t"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["u"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["r"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":27},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":15,"column":36},"action":"insert","lines":["class TestItemModel(TestCase):","","    def test_done_defaults_to_False(self):","        bug = Bugs(title=\"Create a Test\")","        bug.save()","        self.assertEqual(bug.title, \"Create a Test\")","        self.assertFalse(bug.content)","    ","    def test_can_create_an_bug_with_a_name_and_content(self):","        bug = Bugs(title=\"Create a Test\", content=\"Lorem Ipsum\")","        bug.save()","        self.assertEqual(bug.title, \"Create a Test\")","        self.assertTrue(bug.content)"],"id":5}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["g"],"id":6},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["u"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["b"]}],[{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["f"],"id":7},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["a"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["t"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["u"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["r"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["s"],"id":8},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["g"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["u"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["B"]}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["F"],"id":9},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["e"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["a"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["t"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["u"]},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["r"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"remove","lines":["g"],"id":10},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"remove","lines":["u"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["b"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["f"],"id":11},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["e"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["a"]},{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["t"]},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["u"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["r"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"remove","lines":["g"],"id":12},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"remove","lines":["u"]},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"remove","lines":["b"]}],[{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["f"],"id":13},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["e"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["a"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["t"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["u"]},{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["r"]},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"remove","lines":["g"],"id":14},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"remove","lines":["u"]},{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"remove","lines":["b"]}],[{"start":{"row":9,"column":25},"end":{"row":9,"column":26},"action":"insert","lines":["f"],"id":15},{"start":{"row":9,"column":26},"end":{"row":9,"column":27},"action":"insert","lines":["e"]},{"start":{"row":9,"column":27},"end":{"row":9,"column":28},"action":"insert","lines":["a"]},{"start":{"row":9,"column":28},"end":{"row":9,"column":29},"action":"insert","lines":["t"]},{"start":{"row":9,"column":29},"end":{"row":9,"column":30},"action":"insert","lines":["u"]},{"start":{"row":9,"column":30},"end":{"row":9,"column":31},"action":"insert","lines":["r"]},{"start":{"row":9,"column":31},"end":{"row":9,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"remove","lines":["g"],"id":16},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"remove","lines":["u"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"remove","lines":["b"]}],[{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["f"],"id":17},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["e"]},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["a"]},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["t"]},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["u"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["r"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"remove","lines":["g"],"id":18},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"remove","lines":["u"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"remove","lines":["b"]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["f"],"id":19},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"insert","lines":["e"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"insert","lines":["a"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"insert","lines":["t"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"insert","lines":["u"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"insert","lines":["r"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["s"],"id":20},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["g"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["u"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["B"]}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["F"],"id":21},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["e"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["a"]}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":21},"action":"remove","lines":["Fea"],"id":22},{"start":{"row":12,"column":18},"end":{"row":12,"column":25},"action":"insert","lines":["Feature"]}],[{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["g"],"id":23},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":["u"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["b"]}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"insert","lines":["f"],"id":24},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"insert","lines":["e"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"insert","lines":["a"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"insert","lines":["t"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"insert","lines":["u"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"insert","lines":["r"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["g"],"id":25},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["u"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["b"]}],[{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":["f"],"id":26},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["e"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["a"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["t"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["u"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["r"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"remove","lines":["g"],"id":27},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"remove","lines":["u"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"remove","lines":["b"]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["f"],"id":28},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":["e"]},{"start":{"row":15,"column":26},"end":{"row":15,"column":27},"action":"insert","lines":["a"]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":27},"action":"remove","lines":["fea"],"id":29},{"start":{"row":15,"column":24},"end":{"row":15,"column":31},"action":"insert","lines":["feature"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":40},"end":{"row":15,"column":40},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565648796922,"hash":"017acc2025f821685d826059022acf2cf2d69e48"}