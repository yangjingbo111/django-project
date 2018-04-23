from django.db import models

# Create your models here.
class Car(models.Model):
	name = models.CharField(max_length=200)
	place = models.CharField(max_length=200)
	price = models.IntegerField()

	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name