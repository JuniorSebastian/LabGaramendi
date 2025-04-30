# 📰 Portal de Noticias en Django

Este es un proyecto de laboratorio desarrollado con **Django**, donde se implementa un portal de noticias funcional. Tiene un diseño visual con **tema oscuro**, usa plantillas reutilizables y aprovecha el **ORM de Django** para manipular la base de datos sin escribir SQL directamente.

---

## 🚀 Tecnologías Usadas

- Python 3
- Django
- SQLite3
- HTML + CSS (Metodología BEM)
- ORM de Django
- Django Templates
- Pillow (para manejo de imágenes)

---



## ⚙️ Instalación y Configuración

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/portal-noticias-django.git
cd portal-noticias-django
2. Crea y activa el entorno virtual
bash
Copiar
Editar
python -m venv env

# En Windows
env\Scripts\activate

# En Linux/Mac
source env/bin/activate
3. Instala las dependencias
Ya está todo incluido en requirements.txt:

bash
Copiar
Editar
pip install -r requirements.txt
4. Aplica las migraciones y carga datos de ejemplo
bash
Copiar
Editar
python src/manage.py makemigrations
python src/manage.py migrate
python src/manage.py crear_datos
5. Crea un superusuario
bash
Copiar
Editar
python src/manage.py createsuperuser
🔐 Credenciales usadas en este proyecto:

Usuario: admin

Contraseña: admin123

6. Ejecuta el servidor de desarrollo
bash
Copiar
Editar
python src/manage.py runserver
🌐 Portal de Noticias: http://127.0.0.1:8000/

🔧 Panel de Administración: http://127.0.0.1:8000/admin/

🧠 Uso del ORM (Object-Relational Mapping)
El ORM de Django permite trabajar con la base de datos como si fueran objetos Python. Algunos ejemplos implementados en este proyecto:

Articulo.objects.all() para listar artículos

Articulo.objects.filter(categoria=categoria) para mostrar artículos de una categoría específica

Articulo.objects.get(pk=id) para mostrar el detalle de un artículo

Articulo.objects.create(...) para insertar desde el comando crear_datos

Esto evita escribir SQL manualmente, haciéndolo más seguro y mantenible.

🎨 Diseño con BEM y Tema Oscuro
Las plantillas están ubicadas en noticias/templates/noticias/:

base.html: plantilla base con header, footer y estilos oscuros

inicio.html: página principal con artículos destacados

articulo_detail.html: detalle de un artículo

categoria_detail.html: artículos por categoría

Las clases CSS siguen la metodología BEM para mejor organización y escalabilidad de estilos.

🛠 Funcionalidades del Comando crear_datos
Dentro de noticias/management/commands/crear_datos.py se creó un comando personalizado que genera automáticamente:

3 categorías

10 artículos de prueba con contenido y fechas

Asocia los artículos a sus respectivas categorías

Esto es útil para pruebas rápidas sin cargar datos manualmente desde el admin.
