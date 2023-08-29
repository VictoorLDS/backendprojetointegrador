from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Cliente
from jsbackend.serializers import ClienteSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer