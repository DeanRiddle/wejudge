# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-08 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160302_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preference_bgimg',
            field=models.CharField(blank=True, default=b'', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='preference_language',
            field=models.CharField(blank=True, default=b'gcc', max_length=10, null=True),
        ),
    ]
