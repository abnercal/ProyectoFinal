from django.db import models
from django.utils import timezone
# Create your models here.
class Marca(models.Model):#postea algo en el blog
    nombre = models.CharField(max_length=50)


class Bicicleta(models.Model):
    autor = models.ForeignKey('auth.User')
    fabricante=models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion=models.TextField()
    precio=models.FloatField()
    color=models.CharField(max_length=50)
    imagen=models.ImageField(blank = 'True')
    fecha_publicacion = models.DateTimeField(
                        blank=True, null=True)
