# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-07 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20170807_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionstatus',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
