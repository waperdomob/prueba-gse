from django.db import models

# Create your models here.
class Cocteles(models.Model):
    nombre = models.CharField('Nombre del coctel',max_length=50)
    tags = models.CharField('Tags o palabras claves',max_length=100)
    instrucciones = models.CharField('Instrucciones',max_length=200)
    datos_Glass = models.CharField('Datos del vaso o de la copa',max_length=50)
    category = models.CharField('Categoria', max_length=45)
    def __str__(self):
        return self.nombre
    

class Venta(models.Model):
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    descuento = models.DecimalField(default=0.00 , null=True, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return 'f{total}' 
    
class DetVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Cocteles, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.producto.nombre