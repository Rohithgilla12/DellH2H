# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-17 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20190817_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.CharField(default='Hello', max_length=1000),
            preserve_default=False,
        ),
    ]
