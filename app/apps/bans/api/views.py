from apps.bans.api.serializers import BanSerializer
from apps.bans.models import Ban
from rest_framework import generics

class BanList(generics.CreateAPIView):
    queryset = Ban.objects.all()
    serializer_class = BanSerializer