# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-26 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0058_auto_20190423_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Worlds', 'Worlds'), ('Items', 'Items'), ('Base game', 'Base game'), ('Quests', 'Quests'), ('Skills', 'Skills')], default='Base game', max_length=10),
        ),
    ]
