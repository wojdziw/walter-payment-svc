# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-30 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiterappbackend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactionstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
