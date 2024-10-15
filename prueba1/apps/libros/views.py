from django.db.models.query import QuerySet
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from mixins.custom_test_mixin import CustomTestMixin

from .models import Categoria, Libro
from apps.opiniones.forms import OpinionForm
from apps.opiniones.models import Opinion


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
    paginate_by         = 3

    def get_context_data(self) :
        context=super().get_context_data()
        categorias = Categoria.objects.all()
        context["categorias"] = categorias
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset= super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        
        return queryset.order_by('titulo')


def listar_libro_por_categoria(request, categoria):
    categoria_db = Categoria.objects.filter(nombre = categoria)
    libros = Libro.objects.filter(categoria = categoria_db[0].id)
    # Paginación
    paginator = Paginator(libros, 3)  # Muestra 3 libros por página
    page_number = request.GET.get('page')  # Obtiene el número de página de la solicitud
    libros_paginados = paginator.get_page(page_number)  # Obtiene los libros para la página actual

    template_name = 'libros/listar_libros.html'
    context = {
        'libros' : libros_paginados,
        'page_obj': libros_paginados,  # Usa los libros paginados en el contexto(para el paginador)
        'paginator': paginator,  # También pasa el paginator para obtener información de paginación
        'is_paginated': paginator.num_pages > 1,# Determina si la paginación es necesaria
        
    }
    return render(request, template_name=template_name, context=context)

def detalle_libro(request,id):
    libro = Libro.objects.get(id = id)
    opiniones = Opinion.objects.filter(libro = id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.libro = libro
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect('apps.blog_auth:iniciar_sesion')

    context= {
        "libro": libro,
        "form" : form, 
        "opiniones" : opiniones
    }
    template_name = "libros/libro_detalle.html"

    return render(request, template_name=template_name,context=context)

def ordenar_por(request):
    orden = request.GET.get('orden', ' ')
    libros = None

    if orden == 'fecha':
        libros = Libro.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        libros = Libro.objects.order_by('titulo')
    else:
        libros = Libro.objects.all()

    # Paginación
    paginator = Paginator(libros, 3)  # Muestra 3 libros por página
    page_number = request.GET.get('page')  # Obtiene el número de página de la solicitud
    libros_paginados = paginator.get_page(page_number)  # Obtiene los libros para la página actual

    template_name = 'libros/listar_libros.html'
    context = {
        'libros': libros_paginados,
        'page_obj': libros_paginados,  # Usa los libros paginados en el contexto(para el paginador)
        'paginator': paginator,  # También pasa el paginator para obtener información de paginación
        'is_paginated': paginator.num_pages > 1,# Determina si la paginación es necesaria
        
    }
    return render(request, template_name, context)