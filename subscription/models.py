from django.db import models
from registration.models import PatreonUser
from page.models import PatreonPage


class PatreonSubscription(models.Model):
    subuser = models.ForeignKey(PatreonUser, on_delete=models.CASCADE, related_name='fk_4')
    pagesub = models.ForeignKey(PatreonPage, on_delete=models.CASCADE, related_name='fk_5')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dateOpened = models.DateTimeField(auto_now_add=True)
    dateClosed = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
