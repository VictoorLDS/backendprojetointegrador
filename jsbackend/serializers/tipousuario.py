from rest_framework.serializers import ModelSerializer

from jsbackend/models/tipousuario import Tipo_Usuario

class Tipo_UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Tipo_Usuario
        fields = "__all__"
