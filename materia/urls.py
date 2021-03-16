from django.contrib import admin
from django.urls import path
from materia.class_view import MateriaList, MateriaCreate, MateriaUpdate, MateriaDelete

app_name = 'materia'
urlpatterns = [
    path('materia', MateriaList.as_view(), name = 'materia'),
    path('crear_materia/', MateriaCreate.as_view(), name = 'crear_materia'),
    path('editar_materia/<int:pk>/', MateriaUpdate.as_view(), name = 'editar_materia'),
    path('eliminar_materia/<int:pk>/', MateriaDelete.as_view(), name = 'eliminar_materia')

    
]