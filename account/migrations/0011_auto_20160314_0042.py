# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 05:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0010_auto_20160313_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubRepos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_repos', models.CharField(max_length=255, null=True)),
                ('github_repos_hook', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='githubrepos', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos1',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos10',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos10_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos11',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos11_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos12',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos12_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos13',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos13_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos14',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos14_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos15',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos15_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos16',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos16_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos17',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos17_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos18',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos18_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos19',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos19_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos1_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos2',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos20',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos20_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos2_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos3',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos3_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos4',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos4_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos5',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos5_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos6',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos6_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos7',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos7_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos8',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos8_hook',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos9',
        ),
        migrations.RemoveField(
            model_name='account',
            name='github_repos9_hook',
        ),
    ]
