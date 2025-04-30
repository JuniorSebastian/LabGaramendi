from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from noticias.models import Categoria, Articulo
from django.utils.text import slugify
import random

class Command(BaseCommand):
    """Comando para llenar la base de datos con datos de ejemplo"""
    help = 'Llena la base de datos con datos de ejemplo para pruebas y desarrollo'
    
    def handle(self, *args, **options):
        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creando superusuario... 👨‍💼')
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
        
        # Crear categorías de ejemplo
        self.stdout.write('Creando categorías... 📂')
        categorias = [
            'Tecnología',
            'Ciencia',
            'Salud',
            'Política',
            'Entretenimiento'
        ]
        
        for nombre_categoria in categorias:
            Categoria.objects.get_or_create(
                nombre=nombre_categoria,
                slug=slugify(nombre_categoria)
            )
        
        # Obtener todas las categorías y usuarios
        todas_categorias = Categoria.objects.all()
        admin_user = User.objects.get(username='admin')
        
        # Crear artículos de ejemplo
        self.stdout.write('Creando artículos... 📝')
        
        contenidos_ejemplo = [
            "Este es un ejemplo de artículo que contiene información relevante sobre el tema en cuestión. "
            "Los detalles proporcionados aquí son ficticios pero representativos del tipo de contenido "
            "que podría aparecer en un portal de noticias real.",
            
            "La información presentada en este artículo es puramente educativa. Los lectores deben considerar "
            "que este es un proyecto de demostración y que el contenido ha sido generado automáticamente como "
            "parte de un ejercicio de desarrollo web con Django.",
            
            "Los avances recientes en este campo han sido significativos. Expertos de todo el mundo continúan "
            "investigando y desarrollando nuevas técnicas y metodologías. Este artículo ofrece una visión general "
            "de estos desarrollos y sus posibles implicaciones para el futuro.",
            
            "Este artículo examina las tendencias actuales y ofrece perspectivas sobre desarrollos futuros. "
            "Los análisis se basan en datos disponibles públicamente y opiniones de expertos en el campo. "
            "Los lectores deben formar sus propias conclusiones basadas en esta información."
        ]
        
        for i in range(1, 11):  # Crear 10 artículos
            titulo = f"Artículo de Ejemplo {i}"
            
            # Elegir una categoría (ciclando por las disponibles)
            categoria = todas_categorias[i % len(todas_categorias)]
            
            # Elegir un contenido aleatorio
            contenido = random.choice(contenidos_ejemplo)
            
            # Crear artículo
            articulo, creado = Articulo.objects.get_or_create(
                titulo=titulo,
                slug=slugify(titulo),
                defaults={
                    'contenido': contenido,
                    'autor': admin_user,
                    'categoria': categoria,
                    'estado': 'publicado'
                }
            )
            
            if creado:
                self.stdout.write(f' Creado artículo: {titulo} ✅')
            else:
                self.stdout.write(f' El artículo ya existe: {titulo} ℹ️')
        
        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente! 🎉'))