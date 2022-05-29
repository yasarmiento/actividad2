from django.db import models

from apps.marca.models import Marca

# Create your models here.
class Tipovehiculo (models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.ManyToManyField(Marca, through='Vehiculo')
    
    def __str__(self):
        return self.nombre
    
class Vehiculo (models.Model):
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    placa = models.CharField(max_length=30)
    motor = models.CharField(max_length=30)
    marcaid = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tipovehiculoid = models.ForeignKey(Tipovehiculo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.modelo