# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-18 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_userdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='Profile',
        ),
    ]