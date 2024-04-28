# Generated by Django 4.2.4 on 2024-04-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_isla', '0020_rename_detatime_ingreso_asistencia_datetime_ingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='datetime_ingreso',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='datetime_salida',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='motivo_salida',
            field=models.CharField(blank=True, choices=[('fin jornada', 'Fin jornada'), ('proceso ejecutándose', 'Proceso ejecutándose'), ('otro', 'Otro')], max_length=50, null=True),
        ),
    ]
