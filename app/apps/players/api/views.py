from apps.players.api.serializers import PlayerSerializer
from apps.players.models import Player
from rest_framework import generics

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.filter(is_active=True)
    serializer_class = PlayerSerializer
    

class BannedPlayersList(generics.ListAPIView):
    queryset = Player.objects.filter(player_bans__isnull=False).distinct()
    serializer_class = PlayerSerializer