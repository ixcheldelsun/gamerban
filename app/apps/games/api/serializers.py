from apps.games.models import Game

from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    """Game Serializer"""
    
    def valid_name(self, name):
        """Validate name"""
        if Game.objects.filter(name=name).exists():
            raise serializers.ValidationError('Game already exists')
        return name
    
    class Meta:
        model = Game
        fields = ('id', 'name')
        read_only_fields = ('id', )