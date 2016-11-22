from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.articulo_lista),
        url(r'^bicicleta/$', views.Bicicleta_lista),
        url(r'^marca/$', views.Marca_lista),
        url(r'^marca/nuevo/$', views.Marca_nuevo),
        url(r'^marca/(?P<pk>[0-9]+)/editar/$', views.Marca_mod),
        url(r'^marca/(?P<pk>[0-9]+)/eliminar/$', views.Marca_delete),

    ]
