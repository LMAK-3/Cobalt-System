# Generated by Django 4.2.3 on 2023-07-22 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobaltSystemApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='add_user',
            name='birthdate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='add_user',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='add_user',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]