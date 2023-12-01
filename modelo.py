# models.py

from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=255)
    ruc = models.CharField(max_length=20)
    direccion_matriz = models.CharField(max_length=255)
    direccion_sucursal = models.CharField(max_length=255)

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha_emision = models.DateField()
    guia_remision = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class FormaPago(models.Model):
    id_forma_pago = models.AutoField(primary_key=True)
    forma_pago = models.CharField(max_length=255)

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    id_forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

class FacturaAdquirente(models.Model):
    id_factura_adquirente = models.AutoField(primary_key=True)
    nombre_adquirente = models.CharField(max_length=255)
    ruc_adquirente = models.CharField(max_length=20)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

