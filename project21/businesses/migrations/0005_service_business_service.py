# Generated by Django 4.2.11 on 2024-03-12 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0004_remove_service_business_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_business',
            name='service',
            field=models.TextField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
