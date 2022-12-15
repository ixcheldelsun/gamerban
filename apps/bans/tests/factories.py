from factory.django import DjangoModelFactory
from factory import fuzzy, SubFactory
from apps.games.tests.factories import GameFactory
from apps.players.tests.factories import PlayerFactory


class BanFactory(DjangoModelFactory):
    reason = fuzzy.FuzzyChoice(('HARRASMENT', 'CHEATING', 'OTHER'))
    player = SubFactory(PlayerFactory)
    game = SubFactory(GameFactory)
    
    class Meta:
        model = "bans.Ban"
