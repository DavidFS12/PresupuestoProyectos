from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProyectosSerializer, GastosSerializer

class ProyectosViewSet(viewsets.ModelViewSet):
  queryset = Proyecto.objects.all()
  serializer_class = ProyectosSerializer

class GastosViewSet(viewsets.ModelViewSet):
  queryset = Gastos.objects.all()
  serializer_class = GastosSerializer
  

# Create your views here.
