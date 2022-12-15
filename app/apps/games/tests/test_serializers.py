
from apps.games.tests.factories import GameFactory
import pytest
from rest_framework.test import APIRequestFactory
from apps.games.api.serializers import GameSerializer
from apps.games.models import Game
from rest_framework.exceptions import ErrorDetail


class TestGameSerializer:
    
    @pytest.mark.django_db
    def test_valid_data(self):
        request = APIRequestFactory().post('/games')
        
        data = {
            "name": "any_name"
        }
        
        valid_serializer_data = data
        
        serializer = GameSerializer(data=data, context={'request': request})
        
        assert serializer.is_valid(raise_exception=True)
        assert serializer.validated_data == valid_serializer_data
        assert serializer.errors == {}
        
        game = serializer.save()
        
        assert isinstance(game, Game)
        assert game.name == data['name']
        
    
    @pytest.mark.django_db
    def test_invalid_data(self):
        request = APIRequestFactory().post('/games')
        game = GameFactory()
        
        data = {
            "name": game.name
        }
                
        serializer = GameSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'name': [ErrorDetail(string='game with this name already exists.', code='unique')]
        }
        
        
        