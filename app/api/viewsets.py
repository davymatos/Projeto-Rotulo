from rest_framework import viewsets
from app.api import serializers
from app import models

class CategoriasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriasSerializer
    queryset = models.Categoria.objects.all()

class IngredientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IngredientesSerializer
    queryset = models.Ingredientes.objects.all()