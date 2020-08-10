from django.test import TestCase
from adminDashboard.models import Product


class ProductTest(TestCase):
    def setUp(self):
        Product.objects.create(product_name="Grey Color Saree For Women", product_price=6500, product_size="all", product_category="Saree",
                               product_brand="No Brand", product_material="Silk", product_color="Grey", product_photo="/media/images/grey-sari.jpg")
        Product.objects.create(product_name="Windcheater Jacket For Women", product_price=2499, product_size="S, M, L, XL", product_category="Coat, Sweater & Jacket",
                               product_brand="China made", product_material="Cotton Elastene", product_color="Green", product_photo="/media/images/windcheater-jacket.jpg")

    def test_color(self):
        print("Testing color")
        # creating objects
        product1 = Product.objects.get(
            product_name="Grey Color Saree For Women")
        product2 = Product.objects.get(
            product_name="Windcheater Jacket For Women")
        # tesing
        self.assertEqual(product1.product_color, "Grey")
        self.assertEqual(product2.product_color, "Green")

    def test_price(self):
        print("Testing price")
        # creating objects
        product1 = Product.objects.get(
            product_name="Grey Color Saree For Women")
        product2 = Product.objects.get(
            product_name="Windcheater Jacket For Women")
        # tesing
        self.assertEqual(product1.product_price, 6500)
        self.assertEqual(product2.product_price, 2499)

    def test_category(self):
        print("Testing category")
        # creating objects
        product1 = Product.objects.get(
            product_name="Grey Color Saree For Women")
        product2 = Product.objects.get(
            product_name="Windcheater Jacket For Women")
        # tesing
        self.assertEqual(product1.product_category, "Saree")
        self.assertEqual(product2.product_category, "Coat, Sweater & Jacket")
