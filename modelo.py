# models.py

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    # Otros campos del cliente

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Otros campos del producto

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_emision = models.DateField()
    # Otros campos de la factura