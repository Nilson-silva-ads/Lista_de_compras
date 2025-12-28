from django.db import models

# Create your models here.
class Lista_compras(models.Model):
    nome = models.CharField(max_length=100)
    craida_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Item(models.Model):
    lista = models.ForeignKey(Lista_compras, on_delete=models.CASCADE, related_name='itens')
    nome = models.CharField(max_length=100)
    comprado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome