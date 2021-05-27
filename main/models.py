from django.db import models

# Create your models here.

class Offer(models.Model):
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name

class Type(models.Model):
	typeoffer = models.ForeignKey(Offer, on_delete=models.CASCADE)
	kindof = models.CharField(max_length=300)
	description = models.CharField(max_length=700)
	price = models.FloatField()


	def __str__(self):
		return self.kindof