from django.conf.urls import patterns, url
from cajadiaria import views

urlpatterns = [
 url(r'^abrircaja/$', views.abrircaja, name='abrircaja'),
 url(r'^cerrarcaja/$', views.cerrarcaja, name='cerrarcaja'),
 url(r'^cajaabierta/$', views.cajaabierta, name='cajaabierta'),
]
