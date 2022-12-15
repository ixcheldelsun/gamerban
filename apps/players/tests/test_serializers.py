from apps.players.tests.factories import PlayerFactory
from apps.players.models import Player
from apps.players.api.serializers import PlayerSerializer
import pytest
from rest_framework.test import APIRequestFactory
from rest_framework.exceptions import ErrorDetail

class TestBanSerializer:
    
    @pytest.mark.django_db
    def test_valid_data(self):
        request = APIRequestFactory().post('/players')
        
        data = {
            "email": "email@email.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "username": "username"
        }
        
        valid_serializer_data = data
        
        serializer = PlayerSerializer(data=data, context={'request': request})
        
        assert serializer.is_valid(raise_exception=True)
        assert serializer.validated_data == valid_serializer_data
        assert serializer.errors == {}
        
        player = serializer.save()
        
        assert isinstance(player, Player)
        assert player.email == data['email']
        assert player.first_name == data['first_name']
        assert player.last_name == data['last_name']
        assert player.username == data['username']
        
    
    @pytest.mark.django_db
    def test_invalid_data(self):
        request = APIRequestFactory().post('/players')
        player = PlayerFactory()
        
        data = {
            "email": player.email,
            "first_name": "first_name",
            "last_name": "last_name",
            "username": player.username
        }
        
        serializer = PlayerSerializer(data=data, context={'request': request})
        
        assert not serializer.is_valid()
        assert serializer.errors == {
            'username': [ErrorDetail(string='A user with that username already exists.', code='unique')], 
            'email': [ErrorDetail(string='user with this dirección de correo electrónico already exists.', code='unique')]
        }