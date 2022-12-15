from apps.players.api.views import PlayerList, BannedPlayersList
from django.urls import path


urlpatterns = [
    path('players', PlayerList.as_view(), name='player-list'), # list and create players.
    path('players/banned', BannedPlayersList.as_view(), name='banned-players-list'), # list banned players.
]
