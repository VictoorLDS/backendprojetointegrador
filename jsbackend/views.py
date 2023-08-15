from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Categoria
from jsbackend.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer