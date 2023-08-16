from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from jsbackend.views import CategoriaViewSet, CompraViewSet, FornecedorViewSet, MovelViewSet, Tipo_UsuarioViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"compras", CompraViewSet)
router.register(r"fornecedores", FornecedorViewSet)
router.register(r"moveis", MovelViewSet)
router.register(r"tiposusuario", Tipo_UsuarioViewSet)
router.register(r"usuarios", UsuarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]