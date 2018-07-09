from __future__ import unicode_literals

from django.db import models

# Create your models here.
class order_model(models.Model):
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    pnr = models.CharField(max_length=200)
    delivery_station_code = models.CharField(max_length=200)
    train_number = models.CharField(max_length=200)
    ts = models.DateTimeField(auto_now_add=True)
