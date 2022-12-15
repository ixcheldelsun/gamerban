from factory.django import DjangoModelFactory
from factory import Faker


class PlayerFactory(DjangoModelFactory):
    
    username = Faker("user_name")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    
    class Meta:
        model = "players.Player"
        django_get_or_create = ['username', 'email']

