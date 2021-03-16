from django.db import models

class Materia(models.Model):
    idMateria = models.AutoField(primary_key= True) #Campo autoincrementador, clave primaria.
    nombre = models.CharField(max_length= 100 ) #tipo caracter
    sigla = models.CharField(max_length= 50) #tipo caracter
    estado = models.CharField(max_length= 11)

    def __str__(self):
        return self.nombre