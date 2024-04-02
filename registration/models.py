from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class PatreonUser(AbstractUser):
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=128)  # Increase max_length to accommodate hashed passwords
    
    def save(self, *args, **kwargs):
        # Hashed the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
