from django.db import models
from django.forms import DecimalField

class Doctor(models.Model):
    longitude = DecimalField(max_digits=9, decimal_places=6)
    latitude = DecimalField(max_digits=9, decimal_places=6)
    name = models.CharField(max_length=200)
    next_visit = models.DateTimeField('next visit')
