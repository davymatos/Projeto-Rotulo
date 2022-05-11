from django.db import models

class Ingredientes(models.Model):
    ingrediente_id = models.AutoField(primary_key=True, editable=False)
    nome_en = models.CharField(max_length=255)
    nome_alt = models.CharField(max_length=255)
    nome_br = models.CharField(max_length=255)
    origem = models.TextField()
    funcao_principal = models.TextField()
    referencia = models.CharField(max_length=255, default="")
    create_at = models.DateTimeField(auto_now_add=True)