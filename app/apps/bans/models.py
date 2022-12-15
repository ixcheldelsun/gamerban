from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Ban(models.Model):
    reason = models.CharField(_("razón del ban"), max_length=150)
    date = models.DateTimeField(_("fecha del ban"), auto_now=True)
    game = models.ForeignKey('games.Game', on_delete=models.RESTRICT, related_name='game_bans')
    player = models.ForeignKey('players.Player', on_delete=models.RESTRICT, related_name='player_bans')
    
    def __str__(self) -> str:
        return f'{self.player.username} from {self.game} - {self.reason} since {self.date}'