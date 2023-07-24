# Generated by Django 4.2.3 on 2023-07-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobaltSystemApp', '0005_remove_add_user_age_remove_add_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_user',
            name='first_name',
        ),
        migrations.AddField(
            model_name='add_user',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='add_user',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
