from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProductoViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Producto.objects.all().order_by('fecha_caducidad')
        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        producto = Producto.objects.get(id=pk)
        serializer = ProductoSerializer(instance=producto, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)