# Generated by Django 2.1.7 on 2019-03-20 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('foto', models.ImageField(blank=True, upload_to='photos/artistas/%Y/%m/%d/')),
                ('fono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('evaluacion', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]