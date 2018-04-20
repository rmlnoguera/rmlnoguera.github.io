# -*- coding: utf-8 -*-
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

# Create your models here.
class User(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()
	first_name = models.CharField(max_length=30, help_text="First name")
	last_name = models.CharField(max_length=30, help_text="Last name")
	shipping_address = models.CharField(max_length=300, help_text="Shipping address")

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cart_code = models.CharField(max_length=10)
	total_price = models.DecimalField(max_digits=11, decimal_places=2)
	paid_boolean = models.BooleanField()

class Product(models.Model):
	price = models.DecimalField(max_digits=9, decimal_places=2)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

class CartItem(models.Model):
 	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
 	product = models.ForeignKey(Product, on_delete=models.CASCADE)
 	quantity = models.IntegerField(default=0)
 	line_total = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
 		