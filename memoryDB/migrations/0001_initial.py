# Generated by Django 4.0.5 on 2022-08-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db', models.FileField(upload_to='db/db.json', verbose_name='Database')),
            ],
        ),
    ]
