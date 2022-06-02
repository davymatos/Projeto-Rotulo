from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from app.api import serializers
from app import models

class CategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriasSerializer
    queryset = models.Categoria.objects.all()

class IngredientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientesSerializer
    queryset = models.Ingredientes.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['nome_en', 'nome_alt', 'nome_br']
    search_fields = ['nome_en', 'nome_alt', 'nome_br']