from apps.games.api.serializers import GameSerializer
from apps.games.models import Game
from rest_framework import generics

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer