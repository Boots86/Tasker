# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
