from apps.players.models import Player

from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    """Player Serializer"""
    
    class Meta:
        model = Player
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')
        read_only_fields = ('is_active', 'date_joined')
        

class PlayerField(serializers.RelatedField):
    """Custom Related Field for the Player model."""
    
    queryset = Player.objects.all()
    
    
    def to_internal_value(self, data):
        player = Player.get("email", data)
        if not player:
            raise serializers.ValidationError("Player does not exist.")
        return player
    
    def to_representation(self, value):
        return value.email