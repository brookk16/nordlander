# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 00:32
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0021_auto_20190511_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=255),
        ),
    ]
