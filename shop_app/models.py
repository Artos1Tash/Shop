from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    delivery = models.CharField(max_length=128)
    category = models.ForeignKey('shop_app.Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name = models.CharField("Brand", max_length=128)
    description = models.TextField("Description", max_length=1000)
    official_site = models.CharField('Official site', max_length=128)
    product = models.ForeignKey(Product, models.CASCADE)


class ProductComment(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    text = models.TextField()


class ProductLike(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, models.SET_NULL, null=True)
