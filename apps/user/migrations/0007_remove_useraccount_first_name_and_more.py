# Generated by Django 4.2.4 on 2024-01-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_useraccount_persona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
    ]
