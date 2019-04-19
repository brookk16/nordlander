# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0023_auto_20190418_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugs',
            old_name='upvotes',
            new_name='views',
        ),
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('Doing', 'Doing'), ('Fixed', 'Fixed')], default='TODO', max_length=6),
        ),
        migrations.AlterField(
            model_name='bugs',
            name='type',
            field=models.CharField(choices=[('Base game', 'Base game'), ('Quests', 'Quests'), ('Skills', 'Skills'), ('World', 'World'), ('Item', 'Item')], default='Base game', max_length=10),
        ),
    ]