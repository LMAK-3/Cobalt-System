# Generated by Django 4.2.3 on 2023-07-23 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cobaltSystemApp', '0008_add_user_document_add_user_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='add_user',
            name='document',
        ),
        migrations.RemoveField(
            model_name='add_user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='add_user',
            name='last_name',
        ),
    ]
