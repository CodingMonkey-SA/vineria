from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from proveedores.models import Proveedor
from proveedores.forms import ProveedorForm
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
        form = ProveedorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('prov_list')
        return render(request, template_name, {'form':form})
    else:
        return render(request, 'products/login.html',{})

def prov_list(request, template_name='proveedores/proveedor_list.html'):
    if request.user.is_authenticated():
        proveedor = Proveedor.objects.all()
        data = {}
        data['object_list'] = proveedor
        return render(request, template_name, data)
    else:
        return render(request, 'products/login.html', {})

def prov_update(request, pk, template_name='proveedores/new_proveedor.html'):
    if request.user.is_authenticated():
        proveedor = get_object_or_404(Proveedor, pk=pk)
        form = ProveedorForm(request.POST or None, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('prov_list')
        return render(request, template_name, {'form':form})
    else:
        return render(request, 'products/login.html', {})

def prov_delete(request, pk, template_name='proveedores/prov_confirm_delete.html'):
    if request.user.is_authenticated():
        proveedor = get_object_or_404(Proveedor, pk=pk)
        if request.method=='POST':
            proveedor.delete()
            return redirect('prov_list')
        return render(request, template_name, {'proveedor':proveedor})
    else:
        return render(request, 'products/login.html', {})
