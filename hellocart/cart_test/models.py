# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length=30, help_text="First name")
	last_name = models.CharField(max_length=30, help_text="Last name")
	shipping_address = models.CharField(max_length=300, help_text="Shipping address")

class Cart(models.Model):
	cart_code = models.CharField(max_length=10)
	total_price = models.DecimalField(max_digits=11, decimal_places=2)
	paid_boolean = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
	price = models.DecimalField(max_digits=9, decimal_places=2)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)