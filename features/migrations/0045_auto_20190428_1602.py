# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-28 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0044_auto_20190426_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('To do', 'To do'), ('Doing', 'Doing')], default='To do', max_length=14),
        ),
    ]