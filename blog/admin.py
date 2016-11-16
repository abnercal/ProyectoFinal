from django.contrib import admin

# Register your models here.
from .models import Marca,Bicicleta
admin.site.register(Marca)
admin.site.register(Bicicleta)
