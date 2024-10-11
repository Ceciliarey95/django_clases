from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.opiniones.forms import OpinionForm
from .models import Opinion

# Create your views here.

def agregar_opinion(request):
    form = OpinionForm(request.POST)
    if form.is_valid():
        form.save()
        form = OpinionForm()

    template_name= 'opiniones/agregar_opinion.html'
    context = {
        'form' : form,
    }

    return render(request, template_name, context)

def opiniones(request):
    opiniones = Opinion.object.all()
    template_name = 'opiniones/listar_opiniones.html'
    context = {
    'opiniones' : opiniones,
    }
    return render(request, template_name, context)

class ModificarOpinion(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ['texto',]
    template_name = 'opiniones/agregar_opinion.html'
    success_url = reverse_lazy('apps.libros:listar_libros')

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(usuario = self.request.user)
    
class EliminarOpinion(LoginRequiredMixin, DeleteView):
    model = Opinion
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('apps.libros:listar_libros')