from apps.bans.models import Ban
from apps.players.tests.factories import PlayerFactory
from apps.games.tests.factories import GameFactory
import pytest 


class TestBanModel:
    
    @pytest.mark.django_db
    def test_ban_model(self):
        player = PlayerFactory()
        game = GameFactory()
        ban = Ban.objects.create(player=player, game=game, reason="HARRASMENT")
        assert ban.player == player
        assert ban.game == game
        assert ban.reason == "HARRASMENT"
       