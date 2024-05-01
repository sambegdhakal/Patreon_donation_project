from django.db import models
from registration.models import PatreonUser
from page.models import PatreonPage


class PatreonDonation(models.Model):
    pageuser = models.ForeignKey(PatreonUser, on_delete=models.CASCADE, related_name='fk_2')
    pagemodel = models.ForeignKey(PatreonPage, on_delete=models.CASCADE, related_name='fk_3')
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Amount_added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
