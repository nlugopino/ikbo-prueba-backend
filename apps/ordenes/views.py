from django.shortcuts import render
from django.db.models import F
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from apps.producto.models import Producto
import pdb

# Create your views here.
class TipoOrdenViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = TipoOrden.objects.all()
        serializer = TipoOrdenSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrdenesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Ordenes.objects.all()
        serializer = OrdenesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        
        if data["tipo_orden"] == 1 :
            # Orden de ingreso
            Producto.objects.filter(id=data["producto"]).update(
                cantidad=(F('cantidad') + int(data["cantidad"])),
                fecha_caducidad=data["fecha_caducidad"]
            )
        else :
            # Orden de salida
            producto = Producto.objects.get(id=data["producto"])
            if producto.cantidad < int(data["cantidad"]):
                return Response({"error": "No hay suficiente cantidad de producto"}, status=status.HTTP_400_BAD_REQUEST)
            else :
                Producto.objects.filter(id=data["producto"]).update(
                    cantidad=(F('cantidad') - int(data["cantidad"]))
                )

        serializer = OrdenesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()                
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_201_CREATED)