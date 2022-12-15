from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Player(AbstractUser):
    first_name = models.CharField(_('nombre'), max_length=150)
    last_name = models.CharField(_('apellido'), max_length=150)
    
    def __str__(self) -> str:
        return f'{self.username} - {self.first_name} {self.last_name}'