from django.db import models

# Create your models here.
class Item(models.Model):
    nome = models.CharField(max_length=100)
    comprado = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome