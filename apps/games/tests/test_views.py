from rest_framework.test import APITestCase
from apps.games.tests.factories import GameFactory
from apps.games.models import Game
import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.usefixtures('request_factory')
class TestGameView(APITestCase):
    
    def test_create_game(self):
        game = GameFactory()
        total = Game.objects.count()
        
        data = {
            "name": "game"
        }
        
        path = reverse('games_api:games-list')
        resp = self.client.post(
            path,
            data,
            content_type=None
        )
        assert resp.status_code == 201
        assert Game.objects.count() == total + 1
        
    
    def test_get_bans(self):
        for i in range(5):
            GameFactory()
        
        path = reverse('games_api:games-list')
        resp = self.client.get(
            path
        )
        assert resp.status_code == 200
        assert not len(resp.data) == 0