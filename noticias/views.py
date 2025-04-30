from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Articulo, Categoria

class ArticuloListView(ListView):
    """Vista para listar artículos en la página de inicio"""
    model = Articulo
    template_name = "noticias/inicio.html"
    context_object_name = "ultimos_articulos"
    
    def get_queryset(self):
        """Obtener solo artículos publicados"""
        return Articulo.objects.filter(estado="publicado")
    
    def get_context_data(self, **kwargs):
        """Añadir categorías y artículos recientes al contexto"""
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["articulos_recientes"] = Articulo.objects.filter(
            estado="publicado"
        ).order_by("-fecha_publicacion")[:5]
        return context

class ArticuloDetailView(DetailView):
    """Vista para mostrar un solo artículo"""
    model = Articulo
    template_name = "noticias/articulo_detail.html"
    context_object_name = "articulo"
    
    def get_queryset(self):
        """Obtener solo artículos publicados"""
        return Articulo.objects.filter(estado="publicado")
    
    def get_context_data(self, **kwargs):
        """Añadir categorías y artículos recientes al contexto"""
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["articulos_recientes"] = Articulo.objects.filter(
            estado="publicado"
        ).order_by("-fecha_publicacion")[:5]
        return context

class CategoriaDetailView(DetailView):
    """Vista para mostrar una categoría específica"""
    model = Categoria
    template_name = "noticias/categoria_detail.html"
    context_object_name = "categoria"

    def get_queryset(self):
        """Obtenemos solo la categoría que tiene el slug proporcionado"""
        return Categoria.objects.all()

    def get_context_data(self, **kwargs):
        """Añadimos los artículos de la categoría al contexto"""
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()
        context["articulos_categoria"] = Articulo.objects.filter(categoria=categoria, estado="publicado")
        return context