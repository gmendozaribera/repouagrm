from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    sigla = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nombre)


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    ci = models.IntegerField()
    correo = models.CharField(max_length=200)
    celular = models.IntegerField()
    fechaNac = models.DateField()
    registro = models.IntegerField()
    idCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} ".format(self.nombre,self.apellidos)
     