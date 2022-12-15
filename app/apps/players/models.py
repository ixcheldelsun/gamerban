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
    
    @classmethod
    def get(cls, param_str:str, param_value:str) -> bool:
        """Get player by any unique param.
        :param param_str: param to make search on. Can be username or email
        :type param_str: str
        :param param_value: value for param search.
        :type param_value: str
        :raises AttributeError: Only if param is not an attribute of class.
        :return: True if player exists, False otherwise
        :rtype: bool
        """
        
        param = getattr(cls, param_str, None)
        if not param:
            raise AttributeError(f'{cls.__name__} has no attribute {param_str}')
        elif not param.field._unique:
            raise AttributeError(f'Not a valid param to base search, {param_str} is not unique.')
        filter_dict = {f'{param.field.name}':param_value}
        return cls.objects.filter(**filter_dict).first()