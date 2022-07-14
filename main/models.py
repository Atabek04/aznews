from email.mime import image
from django.db import models

class Categories(models.Model):
	category = models.CharField(max_length=200)

	def __str__(self):
		return self.category

class Banner(models.Model):
	poster = models.ImageField()
	
class WnCards(models.Model):
	image = models.ImageField()
	title = models.CharField(max_length=200)
	category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.title

class Followers(models.Model):
	facebook = models.IntegerField()
	instagram = models.IntegerField()
	twitter = models.IntegerField()
	youtube = models.IntegerField()