# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from products.models import Product
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

def index(request, template_name='users/index.html'):
    return render(request, 'users/index.html', {})

def user_list(request, template_name='users/lista_usuarios.html'):
    if request.user.is_authenticated():
        users = User.objects.all()
        data = {}
        data['object_list'] = users
        return render(request, template_name, data)
    else:
        return render(request, 'users/lista_usuarios.html', {})

def user_create(request, template_name='users/registrar_usuario.html'):
    if request.user.is_authenticated():
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('user_list')
        return render(request, template_name, {'form':form})
    else:
        return render(request, 'products/login.html', {})

def user_delete(request,pk, template_name='users/borrar_usuario.html'):
    if request.user.is_authenticated():
        user = get_object_or_404(User, pk=pk)
        if request.method=='POST':
            user.delete()
            return redirect('user_list')
        return render(request, template_name, {'user':user})
    else:
        return render(request, 'products/login.html', {})
