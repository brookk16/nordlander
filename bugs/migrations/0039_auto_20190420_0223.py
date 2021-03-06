# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0038_auto_20190420_0211'),
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
            field=models.CharField(choices=[('Skills', 'Skills'), ('Worlds', 'Worlds'), ('Items', 'Items'), ('Quests', 'Quests'), ('Base game', 'Base game')], default='Base game', max_length=10),
        ),
    ]
