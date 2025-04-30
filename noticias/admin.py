from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Articulo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """Configuración de administración para categorías"""
    list_display = ("nombre", "slug")
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ("nombre",)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    """Configuración de administración para artículos"""
    list_display = ("titulo", "autor", "categoria", "estado", "fecha_publicacion", "mostrar_imagen")
    list_filter = ("estado", "categoria", "fecha_publicacion")
    search_fields = ("titulo", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}
    date_hierarchy = "fecha_publicacion"
    
    def mostrar_imagen(self, obj):
        """Mostrar imagen del artículo"""
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.imagen.url)
        return "Sin imagen"
    
    mostrar_imagen.short_description = "Imagen"