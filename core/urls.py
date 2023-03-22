from django.urls import path

#Vistas
from . import views

# Configuracion de urls
urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]
