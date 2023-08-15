from rest_framework.serializers import ModelSerializer

from jsbackend/models/compra import Compra

from jsbackend/models/compra import ItensCompra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

class ItensCompraCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = "__all__"
