# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-21 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0032_auto_20190420_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='type',
            field=models.CharField(choices=[('Quests', 'Quests'), ('Skills', 'Skills'), ('Worlds', 'World'), ('Items', 'Item')], default='Items', max_length=6),
        ),
    ]