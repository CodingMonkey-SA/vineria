from django.shortcuts import render,redirect
from django.forms import ModelForm
from proveedores.models import Proveedor, Telefono, Direccion
from proveedores.forms import ProveedorForm,TelefonoForm,DireccionForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.views.generic.base import TemplateView
from django.core import serializers
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.template import RequestContext

def prov_create(request, template_name='proveedores/new_proveedor.html'):
    if request.user.is_authenticated():
        form1 = ProveedorForm(request.POST or None)
        form2 = TelefonoForm(request.POST or None)
        form3 = DireccionForm(request.POST or None)
        context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        }
        if form1.is_valid() and form2.is_valid() and form3.is_valid() :
            form1.save()
            form2.save()
            form3.save()
            return redirect('product_list')
        return render(request, template_name, context)
    else:
        return render(request, 'products/login.html',{})
