# Generated by Django 5.0.1 on 2024-01-14 15:28

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitlistapi', '0009_alter_waitlistentry_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistentry',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='US', max_length=128, region=None),
        ),
    ]
