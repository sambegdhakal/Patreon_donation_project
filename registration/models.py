from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from images.models import Image

class PatreonUser(AbstractUser):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=128)  # Increase max_length to accommodate hashed passwords
    profile_image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        # Hashed the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

