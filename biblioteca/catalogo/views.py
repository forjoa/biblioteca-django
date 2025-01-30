from django.views.generic import TemplateView, ListView, DetailView
from .models import Autor, Libro
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import AutorForm, LibroForm

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

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect(reverse('detalle_autor', args=[pk]))
    else:
        form = AutorForm(instance=autor)
    return render(request, 'catalogo/editar_autor.html', {'form': form})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect(reverse('detalle_libro', args=[pk]))
    else:
        form = LibroForm(instance=libro)
    return render(request, 'catalogo/editar_libro.html', {'form': form})

