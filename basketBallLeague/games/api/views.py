from rest_framework import generics
from games.models import Game
from games.api.serializers import GameListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


# Functionality: get all games in sorted order to reflect who won & competition progress
# everyone can access this api call
class GameOrderedList(generics.ListAPIView):

    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['finalscore']

    def get_queryset(self):
        return Game.objects.all()
