from django.urls import path
from . import views

app_name = "noticias"

urlpatterns = [
    # Página de inicio con los últimos artículos
    path("", views.ArticuloListView.as_view(), name="inicio"),

    # Página de detalle del artículo
    path("articulo/<slug:slug>/", views.ArticuloDetailView.as_view(), name="articulo_detail"),

    # Página de detalle de una categoría (usando el slug en lugar de el id)
    path("categoria/<slug:slug>/", views.CategoriaDetailView.as_view(), name="categoria_detail"),
]
