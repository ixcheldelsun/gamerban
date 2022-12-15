from apps.bans.models import Ban
from apps.games.models import Game
from apps.players.models import Player
from apps.players.api.serializers import PlayerSerializer, PlayerField
from rest_framework import serializers


class BanSerializer(serializers.ModelSerializer):
    
    game_id = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all()
    ) 
    email = PlayerField(source='player')
    
    class Meta:
        model = Ban
        fields = ('reason', 'date', 'game_id', 'email')
        read_only_fields = ('date', )
    
    def to_internal_value(self, data):
        data = super(BanSerializer, self).to_internal_value(data)
        data['game'] = data.pop('game_id')
        return data
    
   
        