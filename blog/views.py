from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Marca, Bicicleta
from .forms import MarForm, BiciForm, RegistroForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def logueo(request):
    return render (request,'blog/login.html',{})

def salir(request):
    logout(request)
    return redirect('blog.views.ingreso')

def ingreso(request):
    if request.method =='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario=request.POST['username']
            clave=request.POST['password']
            acceso=authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('blog.views.articulo_lista')
                else:
                    return render(request,'blog/noactivo.html',{})
            else:
                return render(request,'blog/nousuario.html',{})
    else:
        form=AuthenticationForm()
        return render(request,'blog/login.html', {'form': form})


def RegistroUsuario(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog.views.articulo_lista')
    else:
        form = RegistroForm()
    return render(request,'blog/registrar.html', {'form': form})

@login_required(login_url='ingreso')
def articulo_lista(request):
    return render(request, 'blog/base.html',{})

@login_required(login_url='ingreso')
def Bicicleta_lista(request):
    bicicletas=Bicicleta.objects.filter()
    return render(request, 'blog/bicicleta_lista.html', {'bicicletas':bicicletas})

@login_required(login_url='ingreso')
def Bici_nuevo(request):
        if request.method == "POST":
            form = BiciForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('blog.views.Bicicleta_lista')
        else:
            form = BiciForm()
        return render(request, 'blog/createB.html', {'form': form})

@login_required(login_url='ingreso')
def Bici_mod(request, pk):
    post = get_object_or_404(Bicicleta, pk=pk)
    if request.method == "POST":
        form = BiciForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.Bicicleta_lista')
    else:
        form = BiciForm(instance=post)
    return render(request, 'blog/create.html', {'form': form})

@login_required(login_url='ingreso')
def Bici_de(request, pk):
    post = Bicicleta.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog.views.Bicicleta_lista')
    return render(request, 'blog/deleteB.html', {'post': post})

@login_required(login_url='ingreso')
def Marca_lista(request):
    marcas=Marca.objects.all()
    return render(request, 'blog/marca_lista.html', {'marcas':marcas})

@login_required(login_url='ingreso')
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

@login_required(login_url='ingreso')
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

@login_required(login_url='ingreso')
def Marca_delete(request, pk):
        post = Marca.objects.get(pk=pk)
        if request.method == "POST":
            post.delete()
            return redirect('blog.views.Marca_lista')
        return render(request, 'blog/deleteM.html', {'post': post})
