from apps.players.models import Player

from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    """Player Serializer"""
    
    def validate_username(self, username):
        """Validate username"""
        if Player.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        return username
    
    def validate_email(self, email):
        """Validate email"""
        if Player.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        return email
    
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