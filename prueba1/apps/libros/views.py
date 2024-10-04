from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Libro


# Create your views here.

# ------- Categorias -----------------
class CrearCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')

class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')

class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

# ------- Libros -----------------

class CrearLibro(CreateView):
    model = Libro
    fields = ['titulo','autor','descripcion','categoria','imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')

class ActualizarLibro(UpdateView):
    model = Libro
    fields = ['titulo','autor','descripcion','categoria','imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')

class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/listar_libros.html'
    context_object_name = 'libros'
    
