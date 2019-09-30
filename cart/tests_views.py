from django.test import TestCase
from feature.models import Feature
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    
    def test_get_cart_page(self):
        """
        Test to see if correct page is returned when viewing cart
        """
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
    def test_add_to_cart(self):
        """
        Test to see if an item is added to cart
        """
        admin = User(username="admin")
        admin.save()
        feature = Feature(title="test", content="test content", status="done", upvotes=0, views=0,  owner=admin)
        feature.save()
        
        page = self.client.get("/cart/add{0}".format(feature.id))
        session = self.client.session
        session['cart'] = 'cart'
        cart = session['cart']
        
        response = self.client.post("/cart/", kwargs={'feature_id': feature.id})
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        
    def test_adjust_cart(self):
        admin = User(username="admin")
        admin.save()
        feature = Feature(title="test", content="test", status="done", upvotes=0, views=0,  owner=admin)
        feature.save()
        session = self.client.session
        page1 = self.client.get("/cart/add{0}".format(feature.id))
        
        page2 = self.client.get("/cart/adjust{0}".format(feature.id))
        session = self.client.session
        session['cart'] = 'cart'
        cart = session['cart']
        
        quantity = 3
        response = self.client.post("/cart/", kwargs={"feature_id": feature.id},data={"quantity": quantity}, follow=True)
        
        page = self.client.get("/cart/")
        
        self.assertEqual(page.status_code, 200)

        delete_item = self.client.post("/cart/", kwargs={"feature_id": feature.id}, data={"quantity": (quantity - 1)}, follow=True)

        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
        
   