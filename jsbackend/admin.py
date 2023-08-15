from django.contrib import admin

from .models import Categoria, Fornecedor, Movel, Tipo_Usuario, Usuario

admin.site.register(Categoria)
admin.site.register(Fornecedor)
admin.site.register(Movel)
admin.site.register(Tipo_Usuario)
admin.site.register(Usuario)
