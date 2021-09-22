from django.db import models
import random, os
from django.db.models.base import Model

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, default=49.99)
    
    def __str__(self):
        return self.name

