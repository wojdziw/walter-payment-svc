# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-07 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiterappbackend', '0004_delete_greeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionstatus',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
