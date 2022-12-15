from apps.bans.models import Ban
from apps.games.models import Game
from apps.players.api.serializers import PlayerField
from rest_framework import serializers
from apps.bans.api.services import BanService


class BanSerializer(serializers.ModelSerializer):
    """Ban Serializer"""
    
    reason = serializers.ChoiceField(Ban.Reason.choices, required=True)
    game_id = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all()
    ) 
    email = PlayerField(source='player') # using a custom related field for the player email.
    
    class Meta:
        model = Ban
        required_fields = ('reason', 'game_id', 'email')
        fields = ('reason', 'date', 'game_id', 'email')
        read_only_fields = ('date', )
    
    def to_internal_value(self, data):
        data = super(BanSerializer, self).to_internal_value(data)
        data['game'] = data.pop('game_id') # renaming field to match model field. 
        return data
    
    def to_representation(self, instance):
        data = super(BanSerializer, self).to_representation(instance)
        data['reason'] = instance.get_reason_display() # getting the human readable value for the "reason" field.
        return data
    

class BanCheckSerializer(serializers.Serializer):
    """Serializer for checking if a player is banned and also its related ban stats."""
    
    def __init__(self, *args, **kwargs):
        super(BanCheckSerializer, self).__init__(*args, **kwargs)
        self.service = BanService # injecting the service as a class attribute.
    
    email = PlayerField(source='player')
    most_common_reason = serializers.CharField(read_only=True)
    times_reported = serializers.IntegerField(read_only=True)
    games_reported = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Ban
        required_fields = ('email', )
        fields = ('email', 'most_common_reason', 'times_reported', 'games_reported')
        
    def validate(self, attrs):
        player = attrs['player']
        if not player.is_banned:
            raise serializers.ValidationError('Player has not received any reports.')
        return attrs
    
    def create(self, validated_data):
        return validated_data['player'] # returning the player instance as we are not creating anything in DB.
    
    def to_representation(self, instance):
        data = self.service.get_ban_data(instance.id) # getting the ban data from the service.
        data['email'] = instance.email
        return data

    
   
        