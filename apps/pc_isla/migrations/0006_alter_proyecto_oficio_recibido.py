# Generated by Django 4.2.4 on 2024-03-07 18:43

import apps.pc_isla.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_isla', '0005_alter_proyecto_oficio_recibido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='oficio_recibido',
            field=models.FileField(max_length=500, upload_to=apps.pc_isla.models.proyecto_upload_path),
        ),
    ]
