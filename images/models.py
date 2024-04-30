from django.db import models

# Create your models here.
class Image(models.Model):
    image_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)