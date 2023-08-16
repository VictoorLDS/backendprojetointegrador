from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Fornecedor
from jsbackend.serializers import FornecedorSerializer

class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer