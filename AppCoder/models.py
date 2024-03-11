from django.db import models

# Create your models here.

class Estudiantes(models.Model):

    nombre = models.CharField(max_length=60) #texto
    apellido = models.CharField(max_length=60) #texto
    email = models.EmailField(max_length=60) #texto
    edad = models.IntegerField()  #numeros

    def __str__(self):
        return f'{self.apellido} - {self.nombre}'

class Curso(models.Model):

    nombre = models.CharField(max_length=60) #texto
    comision = models.IntegerField()  #numeros

    def __str__(self):
        return f'{self.comision} - {self.nombre}'

class Profesor(models.Model):

    nombre = models.CharField(max_length=60) #texto
    apellido = models.CharField(max_length=60) #texto
    email = models.EmailField(max_length=60) #texto
    profesion = models.CharField(max_length=60) #texto

    def __str__(self):
        return f'{self.apellido} - {self.nombre}'

class Entregable(models.Model):

    nombre = models.CharField(max_length=60) #texto
    fechaEntrega = models.DateField() #fecha
    entregado = models.BooleanField() #TorF

    def __str__(self):
        return f'{self.nombre} - {self.entregado}'

