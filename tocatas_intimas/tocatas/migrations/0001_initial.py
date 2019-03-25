# Generated by Django 2.1.7 on 2019-03-20 20:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tocata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('tipo', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('adhesion', models.IntegerField()),
                ('medio_pago', models.IntegerField()),
                ('flayer', models.ImageField(blank=True, upload_to='photos/flayers/%Y/%m/%d/')),
                ('observaciones', models.TextField(blank=True)),
                ('evaluacion', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('fecha_modificacion', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='artistas.Artista')),
            ],
        ),
    ]