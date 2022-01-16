from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20 ,decimal_places=2)
    seller = models.CharField(max_length=200)
    user = models.ForeignKey(User , on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"
