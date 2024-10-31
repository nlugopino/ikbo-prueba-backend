from rest_framework import serializers
from .models import *
from datetime import datetime, timedelta

class ProductoSerializer(serializers.ModelSerializer):

    estado = serializers.SerializerMethodField('get_estado', read_only=True)
    def get_estado(self, obj):
        if obj.fecha_caducidad is not None:
            hoy = datetime.now().date()
            diferencia = (obj.fecha_caducidad - hoy).days
            if diferencia < 0:
                return "Vencido"
            elif diferencia <= 3:
                return "Por vencer"
            else:
                return "Vigente"
        else :
            return None

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'fecha_caducidad',
            'cantidad',
            'estado',
        ]