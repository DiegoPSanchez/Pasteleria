from django.contrib import admin

#Modelos
from .models import Pedido

# Register your models here.
#admin.site.register(Pedido)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tamaño', 'tipo', 'cliente', 'vendedor','fecha', 'precio')
    list_display_links =('fecha',)
    list_filter = ('fecha', 'tipo', 'vendedor')
    search_fields = ('decoracion', 'vendedor', 'fecha')