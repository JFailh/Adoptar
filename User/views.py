from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from User.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Perro.models import Perro
from Gato.models import Gato


class RegistroUsuarioView(CreateView):
    template_name = 'registro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class HomeClienteView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perros'] = Perro.objects.filter(estado=False)
        context['gatos'] = Gato.objects.filter(estado=False)
        return context
    

class LoginView(TemplateView):
    template_name = 'login.html'