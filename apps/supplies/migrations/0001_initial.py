# Generated by Django 4.2.5 on 2023-10-02 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuxEquipmentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
            ],
            options={
                'verbose_name': 'Modelo base para insumo',
                'verbose_name_plural': 'Modelo base para insumos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EquipmentModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
            ],
            options={
                'verbose_name': 'Modelo base para insumo',
                'verbose_name_plural': 'Modelo base para insumos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FreightModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
            ],
            options={
                'verbose_name': 'Modelo base para insumo',
                'verbose_name_plural': 'Modelo base para insumos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabourModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
                ('fact_real_salary', models.DecimalField(decimal_places=5, default=1, max_digits=5, verbose_name='Factor de salario real')),
                ('is_real_salary', models.BooleanField(default=False, verbose_name='Aplica factor de salario real?')),
            ],
            options={
                'verbose_name': 'Modelo base para insumo',
                'verbose_name_plural': 'Modelo base para insumos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialsFamilyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='SubcontractJobModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
            ],
            options={
                'verbose_name': 'Modelo base para insumo',
                'verbose_name_plural': 'Modelo base para insumos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToolsFamilyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='ToolsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
                ('brand', models.CharField(max_length=50, verbose_name='Marca')),
                ('id_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.toolsfamilymodel', verbose_name='Familia de herramientas')),
            ],
            options={
                'verbose_name': 'Modelo base para insumo',
                'verbose_name_plural': 'Modelo base para insumos',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialsModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(verbose_name='Descripción')),
                ('unit', models.CharField(max_length=15, verbose_name='Unidad de media')),
                ('data_aditional', models.CharField(max_length=50, verbose_name='Datos adicionales')),
                ('brand', models.CharField(blank=True, max_length=50, verbose_name='Marca')),
                ('id_family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies.materialsfamilymodel', verbose_name='Familia del mateiral')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiales',
            },
        ),
    ]