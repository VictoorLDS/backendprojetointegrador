from django.contrib import admin

from jsbackend.models import Categoria, Compra, Fornecedor, ItensCompra, Movel, Usuario

admin.site.register(Categoria)
admin.site.register(Compra)
admin.site.register(Fornecedor)
admin.site.register(ItensCompra)
admin.site.register(Movel)
admin.site.register(Usuario)
