# Generated by Django 4.2.4 on 2024-01-30 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_is_staff_useraccount_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
