from apps.players.api.views import PlayerList
from django.urls import path


urlpatterns = [
    path('players', PlayerList.as_view(), name='player-list'),
]
