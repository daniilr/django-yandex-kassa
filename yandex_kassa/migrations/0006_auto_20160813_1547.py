# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 15:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import yandex_kassa.utils


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_kassa', '0005_auto_20160109_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.CharField(default=yandex_kassa.utils.get_uuid, max_length=64, verbose_name='ID заказа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_number',
            field=models.CharField(default=yandex_kassa.utils.get_uuid, max_length=64, verbose_name='ID плательщика'),
        ),
    ]
