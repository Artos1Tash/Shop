from django.test import TestCase, Client
from django.contrib.auth.models import User
from shop_app.models import Product


class TestProduct(TestCase):
    def test_should_allow_only_get(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/product/")
        assert response.status_code == 200

        response = c.get("http://127.0.0.1:8000/add_to_cart_product")
        assert response.status_code == 200

        response = c.post("http://127.0.0.1:8000/add_to_cart_productt")
        assert response.status_code == 201

        response = c.get("http://127.0.0.1:8000/add_to_cart_product/2/")
        assert response.status_code == 200

        response = c.put("http://127.0.0.1:8000/add_to_cart_product/2/")
        assert response.status_code == 200

        response = c.delete("http://127.0.0.1:8000/add_to_cart_product/2/")
        assert response.status_code == 200

        response = c.get("http://127.0.0.1:8000/add_to_cart")
        assert response.status_code == 200

        response = c.post("http://127.0.0.1:8000/add_to_cart")
        assert response.status_code == 200

        response = c.get("http://127.0.0.1:8000/add_to_cart/2/")
        assert response.status_code == 200

        response = c.post("http://127.0.0.1:8000/add_to_cart/2/")
        assert response.status_code == 200

        response = c.delete("http://127.0.0.1:8000/add_to_cart/2/")
        assert response.status_code == 200


class TestHomepage(TestCase):
    def test_open_homepage_should_be_success(self):
        c = Client()
        response = c.get("http://127.0.0.1:8000/")
        assert response.status_code == 404


    # def test_create_product_with_user(self):
    #     user = User(
    #         username="test1",
    #         email="test1@mail.com",
    #         password="test1",
    #     )
    #     user.save()
    #     print(f"\n{user}\n")
    #     p = Product(
    #         name="яблоко",
    #         price=100,
    #         user=user
    #     )
    #     p.save()
    #
    #     assert user.id == p.user.id
    #     print(f"\nour test done\n")