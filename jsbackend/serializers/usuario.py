from rest_framework.serializers import ModelSerializer

from jsbackend/models/usuario import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
