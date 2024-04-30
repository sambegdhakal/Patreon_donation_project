from django.db import models
from registration.models import PatreonUser
from images.models import Image


class PatreonPage(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(PatreonUser, on_delete=models.CASCADE, related_name='fk_1')
    description = models.TextField()
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner_image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    subscriber_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
