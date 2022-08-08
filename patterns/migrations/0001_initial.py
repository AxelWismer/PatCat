# Generated by Django 4.0.5 on 2022-08-08 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatternType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de patrón',
                'verbose_name_plural': 'Tipos de patrones',
            },
        ),
        migrations.CreateModel(
            name='UseCaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoria de caso de uso',
                'verbose_name_plural': 'Categorias de caso de uso',
            },
        ),
        migrations.CreateModel(
            name='UseCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patterns.usecasecategory', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Caso de uso',
                'verbose_name_plural': 'Casos de uso',
            },
        ),
        migrations.CreateModel(
            name='SmartContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Titulo')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('date', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('business_process', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.usecase', verbose_name='Caso de uso')),
            ],
            options={
                'verbose_name': 'Contrato inteligente',
                'verbose_name_plural': 'Contratos inteligente',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Titulo')),
                ('date', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('editor', models.TextField(verbose_name='Editor')),
                ('abstract', models.TextField()),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.smartcontract', verbose_name='Catálogo')),
            ],
            options={
                'verbose_name': 'Paper',
                'verbose_name_plural': 'Papers',
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('structure', models.TextField(verbose_name='Estructura')),
                ('intent', models.TextField(verbose_name='Intención')),
                ('motivation', models.TextField(verbose_name='Motivación')),
                ('applicability', models.TextField(verbose_name='Aplicación')),
                ('paricipants', models.TextField(verbose_name='Participantes')),
                ('consequences', models.TextField(verbose_name='Consequencias')),
                ('example', models.TextField(verbose_name='Ejemplo')),
                ('related_pattens', models.TextField(verbose_name='Patrones relacionados')),
                ('source_credit', models.TextField(verbose_name='Creditos a la fuente')),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.smartcontract', verbose_name='Catálogo')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.patterntype', verbose_name='Tipo de Patrón')),
            ],
            options={
                'verbose_name': 'Patrón',
                'verbose_name_plural': 'Patrones',
                'unique_together': {('name', 'type')},
            },
        ),
    ]
