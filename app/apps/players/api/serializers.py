from apps.players.models import Player

from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')
        read_only_fields = ('is_active', 'date_joined')
        

class PlayerField(serializers.RelatedField):
    
    queryset = Player.objects.all()
    
    def to_internal_value(self, data):
        return Player.objects.get(email=data)
    
    def to_representation(self, value):
        return value.email