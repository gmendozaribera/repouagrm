from django.contrib import admin
from .models import Trabajo, Semestre,TipoTrabajo,Hashtag,Materia,Grupo,Autor,Fase,Documento
# Register your models here.

admin.site.register(Trabajo)
admin.site.register(Semestre)
admin.site.register(TipoTrabajo)
admin.site.register(Hashtag)
admin.site.register(Materia)

admin.site.register(Grupo)
admin.site.register(Autor)
admin.site.register(Fase)
admin.site.register(Documento)
