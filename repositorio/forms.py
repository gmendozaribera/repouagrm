from django import forms
from . import models
from django.utils.translation import ugettext_lazy as _


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
        labels = {
            'file': _('Documento'),
        }
        widgets = {
        'titulo': forms.TextInput(attrs={'class':'form-control'}),
        'descripcion': forms.Textarea(attrs={'class':'form-control','maxlength':'50','rows':'3'}),
        'file':forms.FileInput(),
        'fase':forms.Select(attrs={'class':'form-control'}),
        'idTrabajo':forms.HiddenInput(),
       
        }

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = models.Trabajo
        fields = [
            'titulo',
            'idPersona',
            'idGrupo',
            'idSemestre',
            'idMateria',
            'idTipoTrabajo',
            'hashtag',
        ]
        widgets = {
        'titulo': forms.TextInput(attrs={'class':'form-control'}),
        'idPersona': forms.HiddenInput(),
        'idGrupo':forms.Select(attrs={'class':'form-control'}),
        'idSemestre':forms.Select(attrs={'class':'form-control'}),
        'idMateria':forms.Select(attrs={'class':'form-control'}),
        'idTipoTrabajo':forms.Select(attrs={'class':'form-control'}),
        'hashtag':forms.SelectMultiple(attrs={'class':'form-control'})
        }
   