from django.db import models

class Tipo_Usuario(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
