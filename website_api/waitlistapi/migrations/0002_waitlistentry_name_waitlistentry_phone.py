# Generated by Django 5.0.1 on 2024-01-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlistapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='waitlistentry',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
