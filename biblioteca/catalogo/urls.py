from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaPrincipal.as_view(), name='pagina_principal'),
    path('autores/', views.ListadoAutores.as_view(), name='listado_autores'),
    path('libros/', views.ListadoLibros.as_view(), name='listado_libros'),
    path('libros/<int:pk>/', views.DetalleLibro.as_view(), name='detalle_libro'),
    path('autores/<int:pk>/', views.DetalleAutor.as_view(), name='detalle_autor'),
]