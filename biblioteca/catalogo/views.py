from django.views.generic import TemplateView, ListView, DetailView
from .models import Autor, Libro

class PaginaPrincipal(TemplateView):
    template_name = "catalogo/pagina_principal.html"

class ListadoAutores(ListView):
    model = Autor
    template_name = "catalogo/listado_autores.html"
    context_object_name = 'autores'

class ListadoLibros(ListView):
    model = Libro
    template_name = "catalogo/listado_libros.html"
    context_object_name = 'libros'

class DetalleLibro(DetailView):
    model = Libro
    template_name = "catalogo/detalle_libro.html"

class DetalleAutor(DetailView):
    model = Autor
    template_name = "catalogo/detalle_autor.html"


