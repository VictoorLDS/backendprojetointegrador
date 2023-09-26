from django.db import models


class Usuario(models.Model):
    class TipoUsuario(models.IntegerChoices):
        CLIENTE = (1,"Cliente",)
        GERENTE = (2,"Gerente",)
        FUNCIONARIO = (3,"Funcionário",)

    tipo = models.IntegerField(choices=TipoUsuario.choices,  default=TipoUsuario.CLIENTE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"