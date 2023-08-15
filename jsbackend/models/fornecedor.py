from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.descricao
            
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"