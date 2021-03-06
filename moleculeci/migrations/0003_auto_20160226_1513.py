# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moleculeci', '0002_auto_20160226_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_name', models.CharField(default='github_name', max_length=255)),
                ('repo_name', models.CharField(default='repo_name', max_length=255)),
                ('repo_path', models.CharField(default='repo_path', max_length=255)),
                ('key', models.CharField(default='key', max_length=255)),
                ('git_cmd', models.CharField(default='git_cmd', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='git_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='github_name',
            field=models.CharField(default='github_name', max_length=255),
        ),
    ]
