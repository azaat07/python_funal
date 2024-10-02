# Generated by Django 5.1.1 on 2024-10-02 12:42

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart_caritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(90)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='KG'),
        ),
    ]