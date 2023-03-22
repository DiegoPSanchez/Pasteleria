from django.urls import path

#Vistas
from reportes.views import ReportSale

# Configuracion de urls
urlpatterns = [
    path('', ReportSale.as_view(), name='reportes'),
]
