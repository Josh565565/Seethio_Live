# Generated by Django 4.2.7 on 2023-11-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauthentication', '0002_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
