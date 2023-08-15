from django.db import models

from jsbackend.models import Tipo_Usuario

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    tipousuario = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT, related_name="usuário")

    def __str__(self):
        return f"{self.username} ({self.tipousuario})"