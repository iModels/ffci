# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20160413_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='reposstatus',
            name='repos_commit_message',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reposstatus',
            name='repos_commit_sha',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='reposstatus',
            name='repos_commit_time',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
