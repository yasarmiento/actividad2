from django.db import models
from apps.vehiculo.models import Vehiculo

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
class Ventas (models.Model):
    fecha = models.CharField(max_length=30)
    valortotal = models.CharField(max_length=30)
    tipopago = models.CharField(max_length=30)
    usuarioid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vehiculo = models.ManyToManyField(Vehiculo, through='Vehiculoventas')
    
    def __str__(self):
        return self.tipopago
    
class Vehiculoventas (models.Model):
    ventasid = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    vehiculoid = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)