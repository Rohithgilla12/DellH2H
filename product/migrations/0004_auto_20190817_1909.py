# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-17 19:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
