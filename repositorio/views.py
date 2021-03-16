from django.shortcuts import render, redirect
from .models import Trabajo, Autor
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import request, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.models import Persona,Carrera
from repositorio.models import Trabajo , Documento
from django.views import generic
from .forms import *
from pathlib import Path
import os
from .detector import detector
from django.db.models import Count
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.

@login_required 
def perfil(request):
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def datos_personales(request,id):
    persona = Persona.objects.get(user=id)
    return render(request, "datos_personales.html",context={'persona':persona})

def trabajos_estudiante(request,id):
    persona = Persona.objects.get(user=id)
    trabajos = Trabajo.objects.filter(idPersona=persona.id).order_by('estado')
    documentos = Documento.objects.values('idTrabajo').annotate(Count('idTrabajo')).order_by()
    print(documentos)
    return render(request, "repositorio/trabajo_estudiante.html",context={'trabajos':trabajos,'documentos':documentos})


def trabajo_detail(request, id):
    documentos = Documento.objects.filter(idTrabajo= id)  
    trabajo = Trabajo.objects.get(id=id)    
    return render(request, "repositorio/trabajo_detail.html",context={"documentos":documentos,"trabajo":trabajo})

def añadir_trabajo(request, id):
    if request.method == 'POST':
        form = TrabajoForm(request.POST)
        if (form.is_valid()):
            documento = form.save()
            persona = Persona.objects.get(id=id)
            return HttpResponseRedirect(reverse('repositorio:trabajos_estudiante',args=([persona.user.pk])))
        else:
            print(form) 
            persona = Persona.objects.get(id=id)
            form = TrabajoForm({'idPersona':persona.id})
            return render(request, "repositorio/trabajo_form.html",context={'form':form,'persona':persona})
    else:
        persona = Persona.objects.get(user=id)
        form = TrabajoForm({'idPersona':persona.id})
        return render(request, "repositorio/trabajo_form.html",context={'form':form,'persona':persona})

def eliminar_trabajo(request, id):
    # Recuperamos la instancia de la persona y la borramos
    
    instancia = Trabajo.objects.get(id=id)
    persona = Persona.objects.get(id=instancia.idPersona.pk)
    instancia.delete()
    # Después redireccionamos de nuevo a la lista
    return HttpResponseRedirect(reverse('repositorio:trabajos_estudiante', args= (persona.user.pk,)))

def añadir_documento(request, id):
    if request.method == 'POST':
        form = DocumentoForm(request.POST,request.FILES)

        if (form.is_valid()):
            documento = form.save()
            print(documento)
            Documento.objects.filter(pk=documento.id).update(idTrabajo=id)
            return HttpResponseRedirect(reverse('repositorio:detalle_trabajo', args= (id,)))
        else: 
            print('invalido')
            trabajo = Trabajo.objects.get(pk=id)
            form = DocumentoForm({'idTrabajo': trabajo.id })
            return render(request, 'repositorio/documento_form.html', {'form':form,'trabajo':trabajo})
    else:
        trabajo = Trabajo.objects.get(id=id)
        form = DocumentoForm({'idTrabajo': trabajo.id })
        return render(request, "repositorio/documento_form.html",context={'form':form,'trabajo':trabajo})


def editar_documento(request, id):
    # Recuperamos la instancia de la persona
    instancia = Documento.objects.get(id=id)
    ruta = 'media/'+ str(instancia.file)
    
    # Creamos el formulario con los datos de la instancia
    form = DocumentoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = DocumentoForm(request.POST,request.FILES, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
           
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            os.remove(os.path.join(BASE_DIR, ruta))
            return HttpResponseRedirect(reverse('repositorio:detalle_trabajo', args=([instancia.idTrabajo.pk])))

    # Si llegamos al final renderizamos el formulario
    return render(request, "repositorio/documento_edit.html", {'form': form,"documento":instancia})


def eliminar_documento(request, id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Documento.objects.get(id=id)
    ruta = 'media/'+ str(instancia.file)
    os.remove(os.path.join(BASE_DIR, ruta))
    instancia.delete()
    # Después redireccionamos de nuevo a la lista
    return HttpResponseRedirect(reverse('repositorio:detalle_trabajo',args=([instancia.idTrabajo.pk])))

def consulta_comparar(request,id):
    documentos = Documento.objects.get(id= id) 
    print(documentos)
    return render(request, "repositorio/consulta_comparar.html",context={"documentos":documentos})

def comparar_documentos(request, id):
    documentos = Documento.objects.get(id= id) 
    ruta = 'media/'+ str(documentos.file)
    if request.method == 'POST':
        alldata = request.POST
        enlace = alldata.get('enlace')
        resultado = detector(enlace,os.path.join(BASE_DIR, ruta))
        return render(request, "repositorio/resultado.html",context={"resultado":resultado,"documento":documentos})
        
    else:
        return render(request, "repositorio/comparar_documento.html",context={"documentos":documentos})

def comparar_local(request, id):
    documento = Documento.objects.get(id=id)
    documentos = Documento.objects.exclude(idTrabajo=documento.idTrabajo)
    ruta1 = 'media/'+ str(documento.file)
    if request.method == 'POST':
        alldata = request.POST
        ruta2 ='media/' + str(alldata.get('documento2'))
        print(ruta2)
        resultado = detector(os.path.join(BASE_DIR, ruta2),os.path.join(BASE_DIR, ruta1))
        return render(request, "repositorio/resultado.html",context={"resultado":resultado,"documento":documento})
    else:
        return render(request, "repositorio/comparar_local.html",context={"documentos":documentos,"documento":documento})

def rechazar_trabajo(request, id):
    documento = Documento.objects.get(id= id)
    Trabajo.objects.filter(id=documento.idTrabajo.pk).update(estado=3)
    return HttpResponseRedirect(reverse('repositorio:listar_trabajos'))
        
def aprobar_trabajo(request, id):
    documento = Documento.objects.get(id= id) 
    if request.method == 'POST':
        alldata = request.POST
        nota = int(alldata.get('nota'))
        Trabajo.objects.filter(id=documento.idTrabajo.pk).update(calificacion=nota)
        Trabajo.objects.filter(id=documento.idTrabajo.pk).update(estado=2)
        return HttpResponseRedirect(reverse('repositorio:listar_trabajos'))
        
    else:
        return render(request, "repositorio/aprobar_form.html",context={"documento":documento})

        
def listar_trabajos(request):
    trabajos = Trabajo.objects.filter(estado=1)
    documentos = Documento.objects.values('idTrabajo').annotate(Count('idTrabajo')).order_by()
    print(documentos)
    return render(request, "repositorio/listar_trabajo.html",context={'trabajos':trabajos,'documentos':documentos})