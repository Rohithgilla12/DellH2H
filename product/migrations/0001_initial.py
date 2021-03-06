# Generated by Django 2.1.1 on 2019-08-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('discountAvilable', models.BooleanField()),
                ('discountPrice', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('specifications', models.TextField()),
            ],
        ),
    ]
