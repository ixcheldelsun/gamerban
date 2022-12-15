from apps.players.models import Player
import pytest 


class TestPlayerModel:
    
    @pytest.mark.django_db
    def test_player_model(self):
        player = Player.objects.create(
            email="email@email.com",
            first_name = "first_name",
            last_name = "last_name",
            username = "username",
        )
        assert player.email == "email@email.com"
        assert player.first_name == "first_name"
        assert player.last_name == "last_name"
        assert player.username == "username"