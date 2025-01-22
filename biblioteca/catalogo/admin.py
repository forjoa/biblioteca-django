from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'anio_publicacion', 'genero', 'isbn', 'autor')
    search_fields = ('titulo', 'autor__nombre')
