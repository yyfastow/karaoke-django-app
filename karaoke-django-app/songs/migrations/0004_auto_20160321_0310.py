# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20160321_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='duration',
            new_name='length',
        ),
    ]
