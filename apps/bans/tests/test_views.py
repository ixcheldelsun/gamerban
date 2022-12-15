from rest_framework.test import APITestCase
from apps.games.tests.factories import GameFactory
from apps.players.tests.factories import PlayerFactory
from apps.bans.tests.factories import BanFactory
from apps.bans.models import Ban
import pytest
from django.urls import reverse

@pytest.mark.django_db
@pytest.mark.usefixtures('request_factory')
class TestBanView(APITestCase):
    
    def test_create_ban(self):
        game = GameFactory()
        player = PlayerFactory()
        total = Ban.objects.count()
        
        data = {
            "reason": "HARRASMENT",
            "game_id": game.id,
            "email": player.email
        }
        
        path = reverse('bans_api:bans-list')
        resp = self.client.post(
            path,
            data,
            content_type=None
        )
        assert resp.status_code == 201
        assert Ban.objects.count() == total + 1
        
    
    def test_get_bans(self):
        for i in range(5):
            BanFactory()
        
        path = reverse('bans_api:bans-list')
        resp = self.client.get(
            path
        )
        assert resp.status_code == 200
        assert not len(resp.data) == 0
        

@pytest.mark.django_db
@pytest.mark.usefixtures('request_factory')
class TestBanCheckView(APITestCase):
    
    def test_check_ban(self):
        player = PlayerFactory()
        for i in range(5):
            game = GameFactory()
            BanFactory(player=player, game=game, reason="HARRASMENT")
        
        data = {
            "email": player.email
        }
        
        path = reverse('bans_api:ban-check')
        resp = self.client.post(
            path,
            data,
            content_type=None
        )
        assert resp.status_code == 201
        assert resp.data == {
            "most_common_reason": "HARRASMENT",
            "times_reported": 5,
            "games_reported": 5,
            "email": player.email
        }
        
        