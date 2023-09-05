from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from uploader.router import router as uploader_router

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
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)

