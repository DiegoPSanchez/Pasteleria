from django.contrib import admin

#models
from .models import Proyectos

# Register your models here.
#admin.site.register(Proyectos)
@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion',)
    list_display_links = ('titulo',)

