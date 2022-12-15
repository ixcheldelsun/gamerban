from apps.bans.api.views import BanList
from django.urls import path


urlpatterns = [
    path('blacklist', BanList.as_view(), name='bans-list'),
]