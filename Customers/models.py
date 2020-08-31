from django.db import models
from myAuth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    Phone2 = models.IntegerField()