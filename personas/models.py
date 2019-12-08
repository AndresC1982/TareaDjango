from django.db import models

# Create your models here.
class Hospital(models.Model):
    personas = []
    consultas = []

class Consulta(models.Model):
    idConsulta = models.IntegerField()
    cantidadPersonas = models.IntegerField()
    nombreEspecialista = models.TextField()
    tipoConsulta = models.TextField()
    estado = models.BooleanField()

class Person(models.Model):
    nombre = models.TextField()
    edad = models.IntegerField()
    noHistoriaClinica = models.IntegerField()
    consulta = models.ForeignKey(Consulta, models.SET_NULL, null=True)
    listaEspera = models.BooleanField()

class Nino(Person):
    peso = models.IntegerField()
    estatura = models.IntegerField()
    #riesgo = (edad * prioridad())/100

    def prioridad(self):
        if int(self.edad) <= 5:
            prioridad = int(self.peso) - int(self.estatura) + 3
        elif int(self.edad) <= 12:
            prioridad = int(self.peso) - int(self.estatura) + 2
        else:
            prioridad = int(self.peso) - int(self.estatura) + 1

        return prioridad

class Joven(Person):
    fumador = models.BooleanField()
    anos_fumando = models.IntegerField(blank=True, null=True)
    #riesgo = (edad * prioridad())/100

    def prioridad(self):
        if self.fumador == True:
            prioridad = int(self.anos_fumando)/4 + 2
        else:
            prioridad = 2

        return prioridad

class Anciano(Person):
    tieneDieta = models.BooleanField()
    #riesgo = (edad * prioridad())/100 + 5.3

    def prioridad(self):
        if self.tieneDieta == True:
            prioridad = int(self.edad)/20 + 4
        else:
            prioridad = int(self.edad)/30 + 3
        
        return prioridad
