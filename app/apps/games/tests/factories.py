from factory.django import DjangoModelFactory
from factory import fuzzy


class GameFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=10)
    
    class Meta:
        model = "games.Game"

