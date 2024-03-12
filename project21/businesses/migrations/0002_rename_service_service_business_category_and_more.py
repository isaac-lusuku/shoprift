# Generated by Django 4.2.11 on 2024-03-12 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service_business',
            old_name='service',
            new_name='category',
        ),
        migrations.AddField(
            model_name='business',
            name='close_time',
            field=models.DateTimeField(default=datetime.time(5, 0)),
        ),
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='business',
            name='open_time',
            field=models.DateTimeField(default=datetime.time(8, 0)),
        ),
    ]