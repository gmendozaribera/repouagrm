from django.db import models

from  users.models import Persona, Carrera
# Create your models here.


class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nombre)


class Semestre(models.Model):
    semestre = models.IntegerField()
    anio = models.IntegerField()
    def __str__(self):
        return "{}-{}".format(self.semestre,self.anio)
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    sigla = models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.nombre)

class Grupo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)
    
class Trabajo(models.Model):
    titulo = models.CharField(max_length=50)
    ESTADOS_OP = (
            (1, 'Entregado'),
            (2, 'Aprobado'),
            (3, 'Rechazado'),
        )
    estado = models.IntegerField(choices=ESTADOS_OP , default=1)
    calificacion = models.IntegerField(default=0)
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=False,blank=False)
    idGrupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True,blank=True)
    idSemestre  = models.ForeignKey(Semestre, on_delete=models.SET_NULL, null=True,blank=True)
    idMateria = models.ForeignKey(Materia, on_delete=models.SET_NULL, null=True,blank=True)
    idTipoTrabajo = models.ForeignKey(TipoTrabajo, on_delete=models.SET_NULL, null=True,blank=True)
    hashtag = models.ManyToManyField("Hashtag")

    def __str__(self):
        return "{}".format(self.titulo)

class Hashtag(models.Model):
    nombre =   models.CharField(max_length=100)
    def __str__(self):
        return "{}".format(self.nombre)

class Autor(models.Model):
    idTrabajo =  models.OneToOneField(Trabajo, on_delete=models.CASCADE)
    idpersona = models.ManyToManyField("users.Persona")
    def __str__(self):
        return "{}".format(self.idpersona)

class Fase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200,null=True)
    def __str__(self):
        return "{}".format(self.nombre)

class Documento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=50)
    file = models.FileField(upload_to = "trabajos")
    idTrabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, null=False,blank=False)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.titulo)