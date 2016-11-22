from django import forms
from .models import Marca,Bicicleta

class MarForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields=('nombre',)
