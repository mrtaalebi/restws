from django.db import models


class Charger(models.Model):
    voltage = models.IntegerField()
    wireless = models.BooleanField()
    factory = models.CharField(max_length=50, null=True)
