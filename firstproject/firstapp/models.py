from django.db import models

# Create your models here.
class Account(models.Model):
    amount = models.FloatField
    currency = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.currency}"