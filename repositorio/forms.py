from django import forms
from . import models


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = models.Documento
        fields = [
            'titulo',
            'descripcion',
            'file',
            'fase',
            'idTrabajo'
        ]

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = models.Trabajo
        fields = [
            'titulo',
            'estado',
            'calificacion',
            'idPersona',
            'idGrupo',
            'idSemestre',
            'idMateria',
            'idTipoTrabajo',
            'hashtag',
        ]
   