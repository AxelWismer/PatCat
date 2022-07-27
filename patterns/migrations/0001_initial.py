# Generated by Django 4.0.5 on 2022-07-27 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Proceso de negocio',
                'verbose_name_plural': 'Procesos de negocio',
            },
        ),
        migrations.CreateModel(
            name='BusinessProcessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoria de proceso de negocio',
                'verbose_name_plural': 'Categorias de procesos de negocio',
            },
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('date', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('business_process', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.businessprocess', verbose_name='Proceso de negocio')),
            ],
            options={
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogos',
            },
        ),
        migrations.CreateModel(
            name='PatternType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de patrón',
                'verbose_name_plural': 'Tipos de patrones',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Titulo')),
                ('date', models.DateField(auto_now=True, verbose_name='Fecha de creacion')),
                ('editor', models.TextField(verbose_name='Editor')),
                ('abstract', models.TextField()),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.catalogue', verbose_name='Catálogo')),
            ],
            options={
                'verbose_name': 'Paper',
                'verbose_name_plural': 'Papers',
            },
        ),
        migrations.AddField(
            model_name='businessprocess',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.businessprocesscategory', verbose_name='Categoria'),
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('structure', models.TextField(verbose_name='Estructura')),
                ('intent', models.TextField(verbose_name='Intención')),
                ('motivation', models.TextField(verbose_name='Motivación')),
                ('applicability', models.TextField(verbose_name='Aplicación')),
                ('paricipants', models.TextField(verbose_name='Participantes')),
                ('consequences', models.TextField(verbose_name='Consequencias')),
                ('example', models.TextField(verbose_name='Ejemplo')),
                ('related_pattens', models.TextField(verbose_name='Patrones relacionados')),
                ('source_credit', models.TextField(verbose_name='Creditos a la fuente')),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.catalogue', verbose_name='Catálogo')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patterns.patterntype', verbose_name='Tipo de Patrón')),
            ],
            options={
                'verbose_name': 'Patrón',
                'verbose_name_plural': 'Patrones',
                'unique_together': {('name', 'type')},
            },
        ),
    ]
