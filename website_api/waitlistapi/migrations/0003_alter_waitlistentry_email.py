# Generated by Django 5.0.1 on 2024-01-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlistapi', '0002_waitlistentry_name_waitlistentry_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistentry',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
