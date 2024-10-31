from rest_framework import serializers
from .models import *

class TipoOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOrden
        fields = [
            'id',
            'nombre',
            'estado',
        ]

class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordenes
        fields = [
            'id',
            'fecha_orden',
            'cantidad',
            'fecha_caducidad',
            'producto',
            'tipo_orden',
        ]