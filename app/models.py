from django.db import models

class Ingredientes(models.Model):
    ingrediente_id = models.AutoField(primary_key=True, editable=False)
    nome_en = models.CharField(max_length=255)
    nome_alt = models.CharField(max_length=255)
    nome_br = models.CharField(max_length=255)
    origem = models.CharField(max_length=255)
    funcao_principal = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)