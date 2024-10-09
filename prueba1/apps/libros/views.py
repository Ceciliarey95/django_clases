from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from mixins.custom_test_mixin import CustomTestMixin

from .models import Categoria, Libro


# Create your views here.

# ------- Categorias -----------------

class CrearCategoria(LoginRequiredMixin,CustomTestMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')

class ActualizarCategoria(UpdateView, CustomTestMixin):
    model = Categoria
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')

class EliminarCategoria(DeleteView, CustomTestMixin):
    model = Categoria
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

# ------- Libros -----------------

class CrearLibro(CreateView , CustomTestMixin):
    model = Libro
    fields = ['titulo','autor','descripcion','categoria','imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')

class ActualizarLibro(UpdateView , CustomTestMixin):
    model = Libro
    fields = ['titulo','autor','descripcion','categoria','imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')

class EliminarLibro(DeleteView, CustomTestMixin):
    model = Libro
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/listar_libros.html'
    context_object_name = 'libros'

    def get_context_data(self) :
        context=super().get_context_data()
        categorias = Categoria.objects.all()
        context["categorias"] = categorias
        return context



def listar_libro_por_categoria(request, categoria):
    categoria_db = Categoria.objects.filter(nombre = categoria)
    libros = Libro.objects.filter(categoria = categoria_db[0].id)
    template_name = 'libros/listar_libros.html'
    context = {
        'libros' : libros
    }
    return render(request, template_name=template_name, context=context)

def detalle_libro(request,id):
    libro = Libro.objects.get(id = id)

    context= {
        "libro": libro
    }
    template_name = "libros/libro_detalle.html"

    return render(request, template_name=template_name,context=context)
    
