from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import MateriaForm
from .models import Materia

class MateriaList(ListView):
    model = Materia
    template_name = 'materia.html'

class MateriaCreate(CreateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'crear_materia.html'
    success_url = reverse_lazy('materia')

class MateriaUpdate(UpdateView):
    model = Materia
    form_class = MateriaForm
    template_name = 'crear_materia.html'
    success_url = reverse_lazy('materia')

class MateriaDelete(DeleteView):
    model = Materia
    template_name = 'verificacion.html'
    success_url = reverse_lazy('materia')