# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0114_auto_20190510_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('To do', 'To do'), ('Doing', 'Doing')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Skills', 'Skills'), ('Items', 'Items'), ('Base game', 'Base game'), ('Quests', 'Quests'), ('Worlds', 'Worlds')], default='Base game', max_length=10),
        ),
    ]
