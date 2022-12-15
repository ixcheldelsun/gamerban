from apps.games.models import Game

from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    """Game Serializer"""
    
    class Meta:
        model = Game
        fields = ('id', 'name')
        read_only_fields = ('id', )