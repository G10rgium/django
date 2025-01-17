from django.db import models

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()


