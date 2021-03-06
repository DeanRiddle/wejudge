# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 03:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20160218_1433'),
        ('asgn', '0004_auto_20160218_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='asgnvisitrequirement',
            name='source_arrangement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_arrangement', to='education.Arrangement'),
        ),
        migrations.AlterField(
            model_name='asgnvisitrequirement',
            name='flag',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
