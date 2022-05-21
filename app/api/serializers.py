from rest_framework import serializers
from app import models

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredientes
        fields = '__all__'