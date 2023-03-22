from django.urls import path

#Vistas
from . import views

# Configuracion de urls
urlpatterns = [
    path('', views.pedidos, name='pedidos'),
    path('<int:id>/', views.pedido, name='pedido'),
    path('<int:id>/complete', views.completado, name='completado'),   
    path('edit/<int:id>/', views.editPedido, name='editPedido'),
    path('add/', views.nuevoPedido, name='addPedido'),
    path('pending/', views.pendientes, name='pendientes'),
    path('end/', views.finalizados, name='finalizados'),
]
