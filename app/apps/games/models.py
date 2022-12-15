from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self) -> str:
        return self.name