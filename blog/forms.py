from django import forms
from .models import  Marca, Bicicleta

class BicicletaForm(forms.ModelForm):

	class Meta:
		model = Bicicleta

		fields = [
			'fabricante',
			'descripcion',
			'precio',
			'color',
		]
		labels = {
			'fabricante': 'Fabricante',
			'descripcion': 'Descripcion',
			'precio': 'Precio',
			'color':'Color',
		}
		widgets = {
			'fabricante': forms.Select(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'precio': forms.TextInput(attrs={'class':'form-control'}),
			'color': forms.TextInput(attrs={'class':'form-control'}),
		}
class MarcaForm(forms.ModelForm):

	class Meta:
		model = Marca
		fields = [
			'nombre',
		]
		labels = {
			'nombre': 'Nombre de la Marca',

		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
		}
