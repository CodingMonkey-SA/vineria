# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from products.models import Product,Venta,VentaProducto,Proveedor
from django.views.generic.base import TemplateView
from django.core import serializers
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Sum,F
from django.db.models.fields import FloatField
import json

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['codigo', 'name', 'productType', 'brand', 'price', 'precio_lista', 'productStock', 'description', 'year', 'variety', 'origin', 'maker', 'size']

def home(request, template_name='products/home.html'):
    if request.user.is_authenticated():
        return render(request, template_name, {})
    else:
        return render(request, 'products/login.html', {})

def ventas(request, template_name='products/vineriaVentas.html'):
    if request.user.is_authenticated():
        id_venta = Venta.objects.filter(estado='BO').values('id')
        if id_venta:
            VentaProducto.objects.filter(venta_id =int(id_venta[0].get('id'))).delete()
            Venta.objects.filter(estado='BO').delete()
        venta = Venta()
        venta.save()
        return render(request, template_name, {})
    else:
        return render(request, 'products/login.html', {})

def product_list(request, template_name='products/product_list.html'):
    if request.user.is_authenticated():
        products = Product.objects.all()
        data = {}
        data['object_list'] = products
        return render(request, template_name, data)
    else:
        return render(request, 'products/login.html', {})

def product_create(request, template_name='products/product_form.html'):
    if request.user.is_authenticated():
        form = ProductForm(request.POST or None)
        if form.is_valid():
            scannedCode = form.data["codigo"]
            matchingProducts = Product.objects.filter(codigo=scannedCode)
            if matchingProducts.count()>0:
                #no escanea y redirije a product_form
                #de nuevo con el parámetro inválido
                return render(request, 'product_form.html', {})
            else:
                form.save()
                return redirect('product_list')
        return render(request, template_name, {'form':form})
    else:
        return render(request, 'products/login.html', {})

def product_update(request, pk, template_name='products/product_edit.html'):
    if request.user.is_authenticated():
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, template_name, {'form':form})
    else:
        return render(request, 'products/login.html', {})

def product_delete(request, pk, template_name='products/product_confirm_delete.html'):
    if request.user.is_authenticated():
        product = get_object_or_404(Product, codigo=pk)
        if request.method=='POST':
            product.delete()
            return redirect('product_list')
        return render(request, template_name, {'product':product})
    else:
        return render(request, 'products/login.html', {})

def login(request, template_name='products/login.html'):
    return render(request, template_name, {})

@csrf_exempt
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        context = {}
        #request_context = RequestContext(request)
        # Redirect to a success page.
        #return render_to_response('Cervezas.html',context,request_context=request_context)
        return render(request,'products/home.html',{})
    else:
        # Show an error page
        return render(request,'products/login.html',{})

def logout_view(request):
    auth.logout(request)
    return render(request,'products/login.html',{})

class DatosProductos(TemplateView):

    def get(self, request, *args, **kwargs):
        id_venta = Venta.objects.filter(estado='BO').values('id')
        cantidad = request.GET['cantidad']
        id_prod = request.GET['pk'];
        try:
            products = Product.objects.get(codigo=id_prod)
            prodexistente= VentaProducto.objects.filter(product_id=id_prod,venta_id=int(id_venta[0].get('id')))
            if prodexistente.count()>0:
                pe = prodexistente[0]
                c = pe.cant
                pe.cant = (c + int(cantidad))
                pe.save()
            else:
                ventaprod = VentaProducto()
                ventaprod.venta_id = int(id_venta[0].get('id'))
                ventaprod.product_id=id_prod
                ventaprod.precio = products.price
                ventaprod.cant=cantidad
                ventaprod.save()
        except Product.DoesNotExist:
            raise Http404("")
        data = serializers.serialize('json',[products])
        return HttpResponse(data, content_type ="application/json")

def realizarventa(request):
    descpesos = request.GET['descpesos']
    descporc = request.GET['descporc']
    id_venta = Venta.objects.filter(estado='BO').values('id')
    venta = Venta(id_venta[0].get('id'))
    sumventas = VentaProducto.objects.filter(venta_id=id_venta[0].get('id')).aggregate(total=Sum(F('precio')*F('cant'), output_field=FloatField()))
    venta.total = sumventas.get('total')
    if (descporc != ''):
       venta.descuento = (venta.total*float(descporc))/100
    if (descpesos != ''):
        venta.descuento = descpesos
    venta.estado = 'CO'
    venta.save()
    response = {}
    return HttpResponse({},'')

def ventarealizada(request):
    return render(request,'products/ventarealizada.html',{})
