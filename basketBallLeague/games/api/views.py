from rest_framework import generics
from games.models import Game
from games.api.serializers import GameListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError


# Functionality: get all games in sorted order to reflect who won & competition progress
# to access the details user must have logged into the system
# details can be accessible only by an admin user

class GameOrderedList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['finalscore']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Game.objects.all()
        else:
            raise ValidationError(
                "Only the admin user can view the game details!")
