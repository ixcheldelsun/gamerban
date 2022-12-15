from apps.bans.api.serializers import BanSerializer, BanCheckSerializer
from apps.bans.models import Ban
from apps.players.tests.factories import PlayerFactory
from apps.games.tests.factories import GameFactory
from apps.bans.tests.factories import BanFactory
import pytest
from rest_framework.test import APIRequestFactory
from rest_framework.exceptions import ErrorDetail

class TestBanSerializer:
    
    @pytest.mark.django_db
    def test_valid_data(self):
        request = APIRequestFactory().post('/blacklist')
        game = GameFactory()
        player = PlayerFactory()
        
        data = {
            "reason": "HARRASMENT",
            "game_id": game.id,
            "email": player.email
        }
        
        valid_serializer_data = {
            "reason": "HARRASMENT",
            "game": game,
            "player": player
        }
        
        serializer = BanSerializer(data=data, context={'request': request})
        
        assert serializer.is_valid(raise_exception=True)
        assert serializer.validated_data == valid_serializer_data
        assert serializer.errors == {}
        
        ban = serializer.save()
        
        assert isinstance(ban, Ban)
        assert ban.reason == "HARRASMENT"
        assert ban.game == game
        assert ban.player == player
        
    
    @pytest.mark.django_db
    def test_invalid_data(self):
        request = APIRequestFactory().post('/blacklist')
        
        data = {
            "reason": "HARRASMENT",
            "game_id": 1,
            "email": "random@correo.com"
        }
        
        serializer = BanSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'game_id': [ErrorDetail(string='Invalid pk "1" - object does not exist.', code='does_not_exist')],
            'email': [ErrorDetail(string='Player does not exist.', code='invalid')]
        }
        
    
    @pytest.mark.django_db
    def test_invalid_reason(self):
        request = APIRequestFactory().post('/blacklist')
        game = GameFactory()
        player = PlayerFactory()
        
        data = {
            "reason": "",
            "game_id": game.id,
            "email": player.email
        }
        
        serializer = BanSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'reason': [ErrorDetail(string='"" is not a valid choice.', code='invalid_choice')]
        }
        
        data = {
            "reason": "TEST",
            "game_id": game.id,
            "email": player.email
        }
        
        serializer = BanSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'reason': [ErrorDetail(string='"TEST" is not a valid choice.', code='invalid_choice')]
        }
        
        
class TestBanCheckSerializer:
    
    @pytest.mark.django_db
    def test_valid_data(self):
        request = APIRequestFactory().post('/blacklist/check')
        player = PlayerFactory()
        for i in range(5):
            game = GameFactory()
            BanFactory(player=player, game=game, reason="HARRASMENT")
        
        data = {
            "email": player.email
        }
        
        valid_serializer_data = {
            "player": player
        }
        
        serializer = BanCheckSerializer(data=data, context={'request': request})
        assert serializer.is_valid(raise_exception=True)
        assert serializer.validated_data == valid_serializer_data
        assert serializer.errors == {}
        
        
    
    @pytest.mark.django_db
    def test_invalid_data(self):
        request = APIRequestFactory().post('/blacklist/check')
        
        data = {
            "email": "random@correo.com"
        }
        
        serializer = BanCheckSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'email': [ErrorDetail(string='Player does not exist.', code='invalid')]
        }
        
    
    @pytest.mark.django_db
    def test_invalid_player(self):
        request = APIRequestFactory().post('/blacklist')
        player = PlayerFactory()
        
        data = {
            "email": player.email
        }
        
        serializer = BanCheckSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'non_field_errors': [ErrorDetail(string='Player has not received any reports.', code='invalid')]
        }
        