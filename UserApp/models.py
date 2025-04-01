from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=18)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=9, unique=True)
    password = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when the object is saved

    def __str__(self):
        return self.username

