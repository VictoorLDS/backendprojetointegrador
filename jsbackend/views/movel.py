from rest_framework.viewsets import ModelViewSet

from jsbackend.models import Movel
from jsbackend.serializers import MovelSerializer

class MovelViewSet(ModelViewSet):
    queryset = Movel.objects.all()
    serializer_class = MovelSerializer