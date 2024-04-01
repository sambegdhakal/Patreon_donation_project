from django.db import models

class User(models.Model):
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=55)