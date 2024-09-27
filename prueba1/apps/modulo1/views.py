from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Modulo1

# ------- CBV -----------------
class CrearRegistro(CreateView):
    model = Modulo1
    fields = ['nombre', 'descripcion']
    template_name = 'modulo1/agregar_registro.html'
    success_url = reverse_lazy('index')

class ActualizarRegistro(UpdateView):
    model = Modulo1
    fields = ['nombre', 'descripcion']
    template_name = 'modulo1/actualizar_registro.html'
    success_url = reverse_lazy('index')

class EliminarRegistro(DeleteView):
    model = Modulo1
    template_name = 'modulo1/confirma_eliminar.html'
    success_url = reverse_lazy('index')

# -------- FBV ---------------
def mostrar_registros(request):
    registros = Modulo1.objects.all()
    contexto = {
        'regitros' : registros
    }
    template = 'modulo1/listar_registros.html'
    return render(request = request, template_name=template, context= contexto)

def mostrar_registro_by_id(request,id):
    registro = Modulo1.objects.get( id = id)
    contexto = {
        'regitro' : registro
    }
    template = 'modulo1/detalle_modulo.html'
    return render(request=request, template_name=template, context = contexto)