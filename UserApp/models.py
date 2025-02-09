from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=18)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=9, unique=True)
    password = models.CharField(max_length=16)


    def __str__(self):
        return self.username