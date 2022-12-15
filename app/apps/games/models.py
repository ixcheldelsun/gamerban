from django.db import models


class Game(models.Model):
    """Game model."""
    
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self) -> str:
        return self.name