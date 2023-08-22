from django.db import models

from jsbackend.models import Categoria, Fornecedor

class Movel(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name="móveis")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="móveis")

    def __str__(self):
        return f"{self.titulo} ({self.preco})"

    class Meta:
        verbose_name = "Móvel"
        verbose_name_plural = "Móveis"