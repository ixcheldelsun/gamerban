from apps.bans.api.services import BanService
from apps.bans.tests.factories import BanFactory
from apps.players.tests.factories import PlayerFactory
from apps.games.tests.factories import GameFactory
import pytest 


class TestBanService:
    
    def __init__(self) -> None:
        self.service = BanService
        self.player = PlayerFactory()
        for i in range(5):
            self.game = GameFactory()
            BanFactory(player=self.player, game=self.game, reason="HARRASMENT")
    
    @pytest.mark.django_db
    def test_number_of_reports(self):
        reports = self.service.get_number_of_reports(self.player)
        assert reports == 5
        
    @pytest.mark.django_db
    def test_number_of_games(self):
        games = self.service.get_number_of_games(self.player)
        assert games == 5
        
    @pytest.mark.django_db
    def test_get_most_common_reason(self):
        reason = self.service.get_most_common_reason(self.player)
        assert reason == "HARRASMENT"
        
    @pytest.mark.django_db
    def test_get_ban_data(self):
        data = self.service.get_ban_data(self.player)
        assert data['reports'] == 5
        assert data['games'] == 5
        assert data['reason'] == "HARRASMENT"
        