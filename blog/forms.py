from django import forms
from .models import Marca,Bicicleta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }

class BiciForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ('fabricante','descripcion','precio','color','imagen',)
class MarForm(forms.ModelForm):
    class Meta:

        model = Marca
        fields = [
			'nombre',
		]
        labels = {
			'nombre': 'Nombre',
		}
        widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
		}
