from django.db import models
from datetime import date


# Create your models here.
class add_user(models.Model):
    name = models.CharField(max_length=30, default='')
    last_name = models.CharField(default='', max_length=100)
    document = models.CharField(default='', max_length=12)
    email = models.EmailField(default='', max_length = 254)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.name