from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('leagues/<str:league>', matches, name='matches'),
    path('deatail/<int:matchid>/', match_detail, name='detail')
]
