from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.
class Marca(models.Model):#postea algo en el blog
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Bicicleta(models.Model):
    autor = models.ForeignKey('auth.User')
    fabricante=models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion=models.TextField()
    precio=models.FloatField()
    color=models.CharField(max_length=50)
    imagen=models.ImageField(null=True,blank = 'True',upload_to='blog/fotos')
    fecha_publicacion = models.DateTimeField(
                        blank=True, null=True)
    def __str__(self):
        return self.descripcion

    def photo_delete(sender, instance, **kwargs):
    #""Borra los ficheros de las fotos que se eliminan""
        instance.imagen.delete(false)
