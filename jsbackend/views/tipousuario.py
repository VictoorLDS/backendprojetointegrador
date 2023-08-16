from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Tipo_Usuario
from jsbackend.serializers import Tipo_UsuarioSerializer

class Tipo_UsuarioViewSet(ModelViewSet):
    queryset = Tipo_Usuario.objects.all()
    serializer_class = Tipo_UsuarioSerializer