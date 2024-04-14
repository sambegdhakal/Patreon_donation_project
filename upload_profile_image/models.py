from django.db import models

class Image(models.Model):
    user_id = models.IntegerField(default=0)  # Assuming user_id is an integer field
    image = models.ImageField(upload_to='images/')
    image_id = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)
    

    def __str__(self):
        return f"Image {self.id} - User {self.user_id}"
