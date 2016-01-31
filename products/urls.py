from django.conf.urls import patterns, url
from products import views
from users import views as usersViews
from proveedores import views as proveedoresViews

urlpatterns = [
  url(r'^products/$', views.product_list, name='product_list'),
  url(r'^new$', views.product_create, name='product_new'),
  url(r'^$', views.home, name='home'),
  url(r'^ventas$', views.ventas, name='ventas'),
  url(r'^edit/(?P<pk>\d+)$', views.product_update, name='product_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.product_delete, name='product_delete'),
  url(r'^login/$', views.login, name='login'),
  url(r'^login_view/$', views.login_view, name='login_view'),
  url(r'^logout_view/$', views.logout_view, name='logout_view'),
  url(r'^datos_prod/$', views.DatosProductos.as_view(), name='datos_prod'),
  url(r'^users/$', usersViews.index, name='index'),
  url(r'^registrar_usuario/$', usersViews.user_create, name='user_create'),
  url(r'^borrar_usuario/(?P<pk>\d+)$', usersViews.user_delete, name='user_delete'),
  url(r'^listar_usuarios/$', usersViews.user_list, name='user_list'),
  url(r'^realizarventa/$', views.realizarventa, name='realizarventa'),
  url(r'^nuevo_proveedor/$', proveedoresViews.prov_create, name='prov_create'),
]
