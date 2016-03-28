# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='%S')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Performer')),
            ],
        ),
        migrations.RemoveField(
            model_name='songs',
            name='performer',
        ),
        migrations.DeleteModel(
            name='Songs',
        ),
    ]