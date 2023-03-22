from django.urls import path

#Vistas
from . import views

# Configuracion de urls
urlpatterns = [
    path('', views.perfil, name='perfil'),
]
