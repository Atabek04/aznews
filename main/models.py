from email.mime import image
from django.db import models

class WnCards(models.Model):
	image = models.ImageField()
	

class Contact(models.Model):
	categories = models.CharField(max_length=200)
	poster = models.ImageField()
	