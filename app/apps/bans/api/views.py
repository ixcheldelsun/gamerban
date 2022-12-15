from apps.bans.api.serializers import BanSerializer, BanCheckSerializer
from apps.bans.models import Ban
from rest_framework import generics


class BanList(generics.ListCreateAPIView):
    """List and create bans for a player."""
    queryset = Ban.objects.all()
    serializer_class = BanSerializer
    
    
class BanCheck(generics.CreateAPIView):
    """Check a player's ban status."""
    queryset = Ban.objects.all()
    serializer_class = BanCheckSerializer