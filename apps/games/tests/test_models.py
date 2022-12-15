from apps.games.models import Game
import pytest


class TestGameModel:
    
    @pytest.mark.django_db
    def test_game_model(self):
        game = Game.objects.create(name="game")
        assert game.name == "game"
        assert game.id == 1