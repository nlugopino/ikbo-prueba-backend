from django.db import models
from apps.producto.models import Producto

# Create your models here.
class TipoOrden(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

class Ordenes(models.Model):
    fecha_orden = models.DateField()
    cantidad = models.IntegerField()
    fecha_caducidad = models.DateField()
    tipo_orden = models.ForeignKey(TipoOrden, on_delete=models.CASCADE, related_name='ordenes_tipo_orden')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ordenes_producto')