# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moleculeci', '0004_auto_20160310_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
