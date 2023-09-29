from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from jsbackend.models import Movel
from uploader.models import Image
from uploader.serializers import ImageSerializer

class MovelSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    
    class Meta:
        model = Movel
        fields = "__all__"

class MovelDetailSerializer(ModelSerializer):
    foto = CharField(source="foto.url")
    class Meta:
        model = Movel
        fields = "__all__"
        depth = 1

class MovelListSerializer(ModelSerializer):
    foto = CharField(source="foto.url")
    class Meta:
        model = Movel
        fields = ["id", "nome", "quantidade", "preco", "fornecedor", "categoria", "foto"]