from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200,
                             default='Noname product')
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    description = models.TextField(default='', blank=True)
    is_active = models.BooleanField(default=False)
    image = models.TextField(default='', blank=True)
    company = models.CharField(max_length=100,
                               default='Noname company')
    category = models.CharField(max_length=100,
                               default='No category')

    def __str__(self):
        return f'Product ID: {self.id}, title: {self.title}'


class MyCart(models.Model):
    key = models.CharField(max_length=200,
                             default='Any key')
    cart = models.TextField(default='',
                            blank=True)

    def __str__(self):
        return f'Session key: {self.key}, In cart: {self.cart}'