from django.db import models

# Create your models here.

class Profile(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    
class UserProfile(models.Model):
    fullname = models.CharField(max_length=60)
    
    