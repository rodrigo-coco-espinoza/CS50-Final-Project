# Generated by Django 4.2.4 on 2024-01-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_is_admin_useraccount_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_buscador_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_buscador_editor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_convenios_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_convenios_editor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_pc_isla_admin',
            field=models.BooleanField(default=False),
        ),
    ]
