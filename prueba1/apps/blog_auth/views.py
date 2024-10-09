from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from .forms import RegistrarseForm

# Create your views here.
class RegistrarseView(FormView):
    template_name = 'users/registrarse.html'
    form_class = RegistrarseForm
    success_url = reverse_lazy('index')

    def form_valid(self, form) :
        form.save()
        return super().form_valid(form)
    
class IniciarSesionView(LoginView):
    template_name = 'users/iniciar_sesion.html'

class EditarPerfil(LoginRequiredMixin ,UpdateView):
    model = User
    form_class = RegistrarseForm
    template_name = 'users/registrarse.html'
    success_url = reverse_lazy('index')  

    def get_object(self, queryset=None):
            return get_object_or_404(User, pk=self.request.user.pk)

    def dispatch(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')
        if str(user_id) != str(request.user.pk):
            raise Http404("No tienes permiso para editar este perfil.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Perfil actualizado correctamente.")
        return super().form_valid(form)
    