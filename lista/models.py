from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length = 100)
    valor = models.IntegerField(default=0)
    

    def __str__(self):
        return self.nome