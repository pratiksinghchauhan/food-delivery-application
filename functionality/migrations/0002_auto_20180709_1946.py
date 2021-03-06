# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-09 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('functionality', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_model',
            name='exprected_delivery_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_model',
            name='isRestaurantNotified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order_model',
            name='status',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
