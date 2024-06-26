# Generated by Django 4.2.4 on 2024-01-30 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pc_isla', '0003_alter_institucion_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='area',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cargo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='subdireccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pc_isla.subdireccion'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
