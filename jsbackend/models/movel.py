from django.db import models

from uploader.models import Image

from jsbackend.models import Categoria, Fornecedor

class Movel(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    cor = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name="móveis")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="móveis")
    foto = models.ForeignKey(
    Image,
    related_name="+",
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    default=None,
    )

    def __str__(self):
        return f"{self.nome} ({self.preco})"

    class Meta:
        verbose_name = "Móvel"
        verbose_name_plural = "Móveis"