# Generated by Django 4.2.3 on 2023-07-22 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cobaltSystemApp', '0003_add_user_email_alter_add_user_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_user',
            name='birthdate',
        ),
    ]