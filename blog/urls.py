from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.articulo_lista),
        url(r'^bicicleta/$', views.Bicicleta_lista),
        url(r'^marca/$', views.Marca_lista),

    ]
