from django.contrib import admin
from .models import Bicicleta
from .models import Marca

# Register your models here.
admin.site.register(Marca)
admin.site.register(Bicicleta)
