from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Compra, ItensCompra
from jsbackend.serializers import CompraSerializer, ItensCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class ItensCompraViewSet(ModelViewSet):
    queryset = ItensCompra.objects.all()
    serializer_class = ItensCompraSerializer