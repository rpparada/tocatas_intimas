from django.db import models
from datetime import datetime

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='photos/artistas/%Y/%m/%d/', blank=True)
    fono = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    evaluacion = models.IntegerField()
    fecha_creacion = models.DateTimeField(default=datetime.now, blank=True)
    fecha_modificacion = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nombre
