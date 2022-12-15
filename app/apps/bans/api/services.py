from apps.bans.models import Ban
from django.db.models import Count


class BanService(object):
    """Service for Ban model"""
    
    
    def get_number_of_reports(player_id:int):
        """Get number of reports for a player"""
        return Ban.objects.filter(player__id=player_id).count()
    
    
    def get_number_of_games(player_id:int):
        """Get number of games where player has been reported."""
        return Ban.objects.filter(player__id=player_id).values('game').distinct().count()
    
    
    def get_most_common_reason(player_id:int):
        """Get most common reason for a player's reports"""
        reason = Ban.objects.filter(player__id=player_id).values('reason').annotate(count=Count('reason')).order_by('-count').first()
        return reason['reason']
    
    
    @classmethod
    def get_ban_data(self, player_id:int):
        """Get ban data for a player"""
        return {
            'most_common_reason': self.get_most_common_reason(player_id),
            'times_reported': self.get_number_of_reports(player_id),
            'games_reported': self.get_number_of_games(player_id)
        }
