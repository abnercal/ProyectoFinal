from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Marca, Bicicleta
from .forms import BicicletaForm
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.
def articulo_lista(request):
    return render(request, 'blog/base.html',{})


def Bicicleta_lista(request):
    bicicletas=Bicicleta.objects.all()
    return render(request, 'blog/bicicleta_lista.html', {'bicicletas':bicicletas})

def Marca_lista(request):
    marcas=Marca.objects.all()
    return render(request, 'blog/marca_lista.html', {'marcas':marcas})
