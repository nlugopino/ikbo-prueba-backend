from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_caducidad = models.DateField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)