# Generated by Django 4.2.3 on 2023-07-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobaltSystemApp', '0002_add_user_age_add_user_birthdate_add_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_user',
            name='email',
            field=models.EmailField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='add_user',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_user',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='add_user',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='add_user',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
