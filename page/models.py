from django.db import models
from registration.models import PatreonUser
# Create your models here.

class PatreonPage(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(PatreonUser, on_delete=models.CASCADE)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title