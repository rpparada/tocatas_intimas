from django.db import models
from datetime import datetime
from artistas.models import Artista

from django.contrib.auth import get_user_model
Usuario = get_user_model()

# Create your models here.
class Tocata(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    tipo = models.IntegerField()
    direccion = models.CharField(max_length=200)
    adhesion = models.IntegerField()
    medio_pago = models.IntegerField()
    flayer = models.ImageField(upload_to='photos/flayers/%Y/%m/%d/', blank=True)
    observaciones = models.TextField(blank=True)
    evaluacion = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    tocata = models.ForeignKey(Tocata, on_delete=models.DO_NOTHING)
    asistente = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True)
    estado = models.IntegerField()
    evaluacion = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(default=datetime.now, blank=True)
