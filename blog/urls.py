from django.conf.urls import include, url
from . import views
from django.conf import settings

urlpatterns = [
        url(r'^home/$', views.articulo_lista),
        url(r'^bicicleta/$', views.Bicicleta_lista),
        url(r'^bicicleta/nuevo/$', views.Bici_nuevo),
        url(r'^bicicleta/(?P<pk>[0-9]+)/editar/$', views.Bici_mod),
        url(r'^bicicleta/(?P<pk>[0-9]+)/eliminar/$', views.Bici_de),
        url(r'^marca/$', views.Marca_lista),
        url(r'^marca/nuevo/$', views.Marca_nuevo),
        url(r'^marca/(?P<pk>[0-9]+)/editar/$', views.Marca_mod),
        url(r'^marca/(?P<pk>[0-9]+)/eliminar/$', views.Marca_delete),
        url(r'^usu/$', views.RegistroUsuario),
        url(r'^$',views.ingreso),
        url(r'^ses$',views.salir),

        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    ]
