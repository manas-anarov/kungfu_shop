from django.db import models
from django.urls import reverse

class Product(models.Model):
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	category = models.IntegerField(default=0,blank=True)
	title = models.CharField(max_length=400, default=0)
	text = models.CharField(max_length=400, default=0)
	price = models.IntegerField(default=0)
	author = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title