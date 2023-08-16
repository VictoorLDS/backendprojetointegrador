from rest_framework.serializers import ModelSerializer

from jsbackend.models import Movel

class MovelSerializer(ModelSerializer):
    class Meta:
        model = Movel
        fields = "__all__"
