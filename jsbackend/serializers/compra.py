from rest_framework.serializers import ModelSerializer

from jsbackend.models import Compra

from jsbackend.models import ItensCompra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
