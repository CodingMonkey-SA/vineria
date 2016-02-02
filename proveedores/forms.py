from django import forms
from .models import Proveedor
from django.forms import ModelForm

class ProveedorForm (forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
