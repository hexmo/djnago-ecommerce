from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField(default=0)
    product_size = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    product_brand = models.CharField(max_length=200)
    product_material = models.CharField(max_length=20)
    product_color = models.CharField(max_length=20)
    product_photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return (self.product_name + ' , Nrs: ' + str(self.product_price))


class Cart(models.Model):
    cart_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Address(models.Model):
    address_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address_district = models.CharField(max_length=50)
    address_city = models.CharField(max_length=50)
    address_street = models.CharField(max_length=250)


class Order(models.Model):
    order_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_address = models.ForeignKey(Address, on_delete=models.CASCADE)
