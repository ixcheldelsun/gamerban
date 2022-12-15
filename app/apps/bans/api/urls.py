from apps.bans.api.views import BanList, BanCheck
from django.urls import path


urlpatterns = [
    path('blacklist', BanList.as_view(), name='bans-list'), # list and create bans for a player.
    path('blacklist/check', BanCheck.as_view(), name='ban-check') # check a player's ban status.
]