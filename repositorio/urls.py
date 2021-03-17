from django.contrib import admin
from django.urls import path
from repositorio.views import *

app_name = 'repositorio'
urlpatterns = [
    path('inicio/', perfil, name='inicio'),
    path('user/datos/<id>',datos_personales, name= 'datos_personales'),
    path('user/trabajos/<id>',trabajos_estudiante, name= 'trabajos_estudiante'), 
    path('user/<id>/addtrabajo',añadir_trabajo, name= 'añadir_trabajo'),
    path('trabajo/<id>/',trabajo_detail, name= 'detalle_trabajo'),
    path('trabajos/listar',listar_trabajos, name= 'listar_trabajos'),
    path('trabajos/<id>/consulta_comparar',consulta_comparar, name= 'consulta_comparar'),
    path('trabajos/<id>/comparar_local',comparar_local, name= 'comparar_local'),
    path('trabajo/<int:id>/addocument',añadir_documento, name= 'añadir_documento'),
    path('trabajo/<id>/eliminar',eliminar_trabajo, name= 'eliminar_trabajo'),
    path('trabajo/<id>/eleminardocumento',eliminar_documento, name= 'eliminar_documento'),
    path('trabajo/<id>/editardocumento',editar_documento, name= 'editar_documento'), 
    path('comparar/<id>/documento',comparar_documentos, name= 'comparar_documentos'),
    path('rechazar/<id>/documento',rechazar_trabajo, name= 'rechazar_trabajo'),
    path('aprobar/<id>/documento',aprobar_trabajo, name= 'aprobar_trabajo'),

    
]