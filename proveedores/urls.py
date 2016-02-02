from django.conf.urls import patterns, url
from proveedores import views

urlpatterns = [
  url(r'^nuevo_proveedor/$', views.prov_create, name='prov_create'),
  url(r'^proveedores/$', views.prov_list, name='prov_list'),
  url(r'^edit_prov/(?P<pk>\d+)$', views.prov_update, name='prov_edit'),
  url(r'^delete_prov/(?P<pk>\d+)$', views.prov_delete, name='prov_delete'),
]
