# Generated by Django 4.2.4 on 2024-01-26 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pc_isla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='backup_sii',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='backup_sii_proyecto', to='pc_isla.persona'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='encargado_sii',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='encargado_sii_proyecto', to='pc_isla.persona'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='institucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pc_isla.institucion'),
        ),
        migrations.AddField(
            model_name='persona',
            name='institucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pc_isla.institucion'),
        ),
        migrations.AddField(
            model_name='persona',
            name='subdireccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pc_isla.subdireccion'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='ministerio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pc_isla.institucion'),
        ),
    ]
