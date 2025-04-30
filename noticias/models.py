from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Categoria(models.Model):
    """Modelo de categoría para organizar artículos"""
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        """Genera el slug automáticamente si no está presente"""
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Genera la URL para acceder al detalle de la categoría"""
        return reverse("noticias:categoria_detail", kwargs={"slug": self.slug})


class Articulo(models.Model):
    """Modelo de artículo de noticias"""
    OPCIONES_ESTADO = (
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
    )
    
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="articulos/", blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=OPCIONES_ESTADO, default="borrador")
    
    # Relaciones
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="articulos")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articulos")

    class Meta:
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        """Genera el slug automáticamente si no está presente"""
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Genera la URL para acceder al detalle del artículo"""
        return reverse("noticias:articulo_detail", kwargs={"slug": self.slug})
