from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class PatreonUser(AbstractUser):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=128)  # Increase max_length to accommodate hashed passwords
    
    def save(self, *args, **kwargs):
        # Hashed the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

# Specify unique related_name arguments for the conflicting fields
PatreonUser._meta.get_field('groups').remote_field.related_name = 'patreon_user_groups'
PatreonUser._meta.get_field('user_permissions').remote_field.related_name = 'patreon_user_permissions'