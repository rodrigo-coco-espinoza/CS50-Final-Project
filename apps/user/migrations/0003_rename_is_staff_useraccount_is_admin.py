# Generated by Django 4.2.4 on 2024-01-30 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_is_editor_useraccount_is_pc_isla_editor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
