from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Usuario
from jsbackend.serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer