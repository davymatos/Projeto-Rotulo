from rest_framework import serializers
from app import models

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredientes
        fields = '__all__'