# Generated by Django 2.1.7 on 2019-03-22 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tocatas', '0002_asistencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='asistente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
