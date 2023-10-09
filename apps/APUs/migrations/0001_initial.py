# Generated by Django 4.2.5 on 2023-10-09 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplies', '0003_alter_auxequipmentmodel_data_aditional_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisOfUnitaryPricesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500, verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de medida')),
                ('key_user_item', models.CharField(max_length=15, verbose_name='Código')),
                ('id_user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialsRelationshipModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cant', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Costo total')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de creación')),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora de modificación')),
                ('date_delete', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora de eliminación')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('id_APU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APUs.analysisofunitarypricesmodel', verbose_name='APU')),
                ('id_materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.materialsmodel', verbose_name='Material')),
                ('id_user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id usuario que creo el insumo')),
            ],
            options={
                'verbose_name': 'Relación materiales - APU',
                'verbose_name_plural': 'Relaciones materiales - APU',
            },
        ),
        migrations.CreateModel(
            name='LabourRelarionshipModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cant', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Costo total')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora de creación')),
                ('date_edit', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora de modificación')),
                ('date_delete', models.DateTimeField(auto_now=True, verbose_name='Fecha y hora de eliminación')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('id_APU', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APUs.analysisofunitarypricesmodel', verbose_name='APU')),
                ('id_labour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.labourmodel', verbose_name='Mano de obra')),
                ('id_user_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id usuario que creo el insumo')),
            ],
            options={
                'verbose_name': 'Relación mano de obra - APU',
                'verbose_name_plural': 'Relaciones mano de obra - APU',
            },
        ),
    ]
