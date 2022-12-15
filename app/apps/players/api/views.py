from apps.players.api.serializers import PlayerSerializer
from apps.players.models import Player
from rest_framework import generics

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer