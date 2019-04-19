# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_auto_20190418_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('World', 'World'), ('Item', 'Item'), ('Skills', 'Skills'), ('Quests', 'Quests')], default='Item', max_length=6),
        ),
    ]