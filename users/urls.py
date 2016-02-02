from django.conf.urls import patterns, url
from users import views

urlpatterns = [
  url(r'^users/$', views.index, name='index'),
  url(r'^registrar_usuario/$', views.user_create, name='user_create'),
  url(r'^borrar_usuario/(?P<pk>\d+)$', views.user_delete, name='user_delete'),
  url(r'^listar_usuarios/$', views.user_list, name='user_list'),
]
