from django.test import TestCase, Client
from django.contrib.auth.models import User
from shop_app.models import Product, Category


class TestProduct(TestCase):
    def test_should_allow_only_get(self):
        c = Client()

        response = c.post("http://127.0.0.1:8000/product/")
        assert response

        response = c.get("http://127.0.0.1:8000/product/")
        assert response.status_code == 200

        response = c.get("http://127.0.0.1:8000/add_to_cart_product")
        assert response.status_code == 200

        response = c.post("http://127.0.0.1:8000/add_to_cart_product")
        assert response



class TestHomepage(TestCase):
    def test_open_homepage_should_be_success(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/")
        assert response.status_code == 404

    # def test_create_product_with_user(self):
    #     user = User(
    #         username="test1",
    #         password="test1",
    #     )
    #     user.save()
    #     # print(f"\n{user}\n")
    #     p = Product(
    #         name="apple",
    #         price=100,
    #         user=user
    #     )
    #     p.save()
    #
    #     assert user.id == p.user.id
    #     # print(f"\nour test done\n")
