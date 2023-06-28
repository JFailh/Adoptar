from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Perro.models import Perro

class PerroList(ListView,LoginRequiredMixin):
    model = Perro
    template_name = 'perro_list.html'
    context_object_name = 'perros'

class PerroCreate(CreateView,LoginRequiredMixin):
    model = Perro
    template_name = 'perro_form.html'
    fields = ['nombre','edad','raza']
    success_url = reverse_lazy('perrolist')


class PerroDetail(DetailView,LoginRequiredMixin):
    model = Perro
    template_name = 'perro_detail.html'
    context_object_name = 'perro'

class PerroUpdate(UpdateView,LoginRequiredMixin):
    model = Perro
    template_name = 'perro_form.html'
    fields = ['nombre','edad','raza']
    success_url = reverse_lazy('perrolist')


class PerroAdopt(DeleteView,LoginRequiredMixin):
    model = Perro
    template_name = 'perro_adopt.html'
    success_url = reverse_lazy('home')