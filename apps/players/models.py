from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Player(AbstractUser):
    """Player model for users."""
    email = models.EmailField(_("dirección de correo electrónico"), unique=True)
    first_name = models.CharField(_('nombre'), max_length=150)
    last_name = models.CharField(_('apellido'), max_length=150)
    
    def __str__(self) -> str:
        return f'{self.username} - {self.first_name} {self.last_name}'
    
    @property
    def is_banned(self):
        return self.player_bans.exists()
    
