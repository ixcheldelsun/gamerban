from apps.games.api.views import GameList
from django.urls import path


urlpatterns = [
    path('games', GameList.as_view(), name='games-list'),
]