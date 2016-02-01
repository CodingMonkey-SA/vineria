from cajadiaria.models import CajaDiaria
from django import forms
from django.forms import ModelForm

class CajaDiariaForm(forms.ModelForm):

    class Meta:
        model = CajaDiaria
        fields = ('saldoinicial',)