from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Gato.models import Gato

class GatoList(ListView,LoginRequiredMixin):
    model = Gato
    template_name = 'gato_list.html'
    context_object_name = 'gatos'

class GatoCreate(CreateView,LoginRequiredMixin):
    model = Gato
    template_name = 'gato_form.html'
    fields = ['nombre','edad','raza']
    success_url = reverse_lazy('gatolist')


class GatoDetail(DetailView,LoginRequiredMixin):
    model = Gato
    template_name = 'gato_detail.html'
    context_object_name = 'gato'

class GatoUpdate(UpdateView,LoginRequiredMixin):
    model = Gato
    template_name = 'gato_form.html'
    fields = ['nombre','edad','raza']
    success_url = reverse_lazy('gatolist')


class GatoAdopt(DeleteView,LoginRequiredMixin):
    model = Gato
    template_name = 'gato_adopt.html'
    success_url = reverse_lazy('home')