# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-04 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='is_recommend',
        ),
        migrations.AddField(
            model_name='article',
            name='icon',
            field=models.ImageField(null=True, upload_to='article'),
        ),
    ]
