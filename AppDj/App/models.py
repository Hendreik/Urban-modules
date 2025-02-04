from django.db import models
from django.db.models import fields

# Create your models here.
class Client(models.Model):
	id=models.Field
	name=models.CharField(max_length=100)
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	age = models.IntegerField()

class Buyer (models.Model):
	name = models.CharField(max_length=20)
	balance =models.DecimalField(max_digits=10,decimal_places=2)
	age =models.IntegerField()

	def __str__(self):
		return self.name

class Game(models.Model):
	title =models.CharField(max_length=100)
	cost =models.DecimalField(max_digits=10,decimal_places=2)
	size =models.DecimalField(max_digits=10,decimal_places=2)
	description =models.TextField(blank=True)
	age_limited =models.BooleanField(default= False)
#	buyer =models.ManyToManyField(Buyer,related_name='buyer')

class News (models.Model):
	title = models.CharField(max_length=100)
	content =models.TextField()
	date =models.DateTimeField(auto_now=True)
''''
'''
