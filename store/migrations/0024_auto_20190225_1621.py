# Generated by Django 2.0.8 on 2019-02-25 21:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_couponuser_uniqueness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='percent_off',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Percentage off'),
        ),
        migrations.AlterField(
            model_name='historicalcoupon',
            name='percent_off',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Percentage off'),
        ),
    ]
