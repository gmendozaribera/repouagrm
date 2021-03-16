from django.shortcuts import render, redirect
from .models import Materia
from .forms import MateriaForm

#se usará en urls.py, retorna la vista materia.html
def inicio(request):
    materias = Materia.objects.all() 
    contexto = {
        'materias':materias
    }
    return render(request,'materia.html', contexto)


def crearMateria(request):
    if request.method == 'GET': #si es por get, mostrar formulario
        form = MateriaForm()
        contexto = {
        'form':form
    }
    else:
        form = MateriaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('materia')
    return render(request, 'crear_materia.html', contexto)


#edita por id,se obtiene la materia, si existe ese id, se llena el form, si no, se envían los datos y se edita.
def editarMateria(request,id):
    materia = Materia.objects.get(id = id)
    if request.method == 'GET':
        form = MateriaForm(instance = materia)
        contexto = {
            'form':form
        }
    else:
        form = MateriaForm(request.POST, instance = materia)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('materia')
    return render(request, 'crear_materia.html', contexto)


def eliminarMateria(request,id):
    materia = Materia.objects.get(id = id)
    materia.delete()
    return redirect('materia')