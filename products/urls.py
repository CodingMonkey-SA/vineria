from django.conf.urls import patterns, url
from products import views
from users import views as usersViews

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
  url(r'^realizarventa/$', views.realizarventa, name='realizarventa'),
]
