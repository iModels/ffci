# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 20:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_fix_str'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2016, 3, 10, 14, 23, 1, 895963)),
        ),
    ]
