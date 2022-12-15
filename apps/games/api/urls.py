from apps.games.api.views import GameList
from django.urls import path

app_name = 'games_api'

urlpatterns = [
    path('games', GameList.as_view(), name='games-list'), # list and create games.
]