from django import forms
from .models import Proveedor, Telefono, Direccion
from django.forms import ModelForm

class ProveedorForm (forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class TelefonoForm (forms.ModelForm):
    class Meta:
        model = Telefono
        exclude = ['proveedor']


class DireccionForm (forms.ModelForm):
    class Meta:
        model = Direccion
        exclude = ['proveedor']
