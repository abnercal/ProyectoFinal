from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Marca, Bicicleta
from .forms import MarForm
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone

# Create your views here.
def articulo_lista(request):
    return render(request, 'blog/base.html',{})


def Bicicleta_lista(request):
    bicicletas=Bicicleta.objects.all()
    return render(request, 'blog/bicicleta_lista.html', {'bicicletas':bicicletas})

def Marca_lista(request):
    marcas=Marca.objects.all()
    return render(request, 'blog/marca_lista.html', {'marcas':marcas})


def Marca_nuevo(request):
        if request.method == "POST":
            form = MarForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('blog.views.Marca_lista')
        else:
            form = MarForm()
        return render(request, 'blog/create.html', {'form': form})

def Marca_mod(request, pk):
        post = get_object_or_404(Marca, pk=pk)
        if request.method == "POST":
            form = MarForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('blog.views.Marca_lista')
        else:
            form = MarForm(instance=post)
        return render(request, 'blog/create.html', {'form': form})

def Marca_delete(request, pk):
        post = Marca.objects.get(pk=pk)
        if request.method == "POST":
            post.delete()
            return redirect('blog.views.Marca_lista')
        return render(request, 'blog/deleteM.html', {'post': post})
