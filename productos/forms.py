from django import forms
from .models import Producto, Embarque

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EmbarqueForm(forms.ModelForm):
    class Meta:
        model = Embarque
        fields = ['codigo_rastreo', 'fecha_llegada', 'productos']
        widgets = {
            'codigo_rastreo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_llegada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '10'}),
        }