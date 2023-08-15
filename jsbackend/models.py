from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.descricao
            
    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"


class Movel(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name="móveis")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="móveis")

    def __str__(self):
        return f"{self.titulo} ({self.preco})"

class Tipo_Usuario(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    tipousuario = models.ForeignKey(Tipo_Usuario, on_delete=models.PROTECT, related_name="usuário")

    def __str__(self):
        return f"{sefl.username} ({self.tipousuario})"
