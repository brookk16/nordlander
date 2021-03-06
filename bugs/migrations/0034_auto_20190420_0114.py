# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-20 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0033_auto_20190419_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Fixed', 'Fixed')], default='To do', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Items', 'Items'), ('Quests', 'Quests'), ('Base game', 'Base game'), ('Skills', 'Skills'), ('Worlds', 'Worlds')], default='Base game', max_length=10),
        ),
    ]
