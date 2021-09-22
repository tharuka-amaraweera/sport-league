from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
import json
from rest_framework.permissions import IsAuthenticated

from users.models import Player
from users.api.serializers import (PlayersScoreListSerializer, PlayersPersonalDetailsListSerializer,
                                   NintyPercentilePlayersListSerializer)
from users.api.permissions import TeamCoachOrAdmin
from users.api.datacalculations import Calculate


# Functionality:  get list of players with their average scores
# to access the details user must have logged into the system
# details can be accessible only by an admin user or the coach of their team


class PlayerList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlayersScoreListSerializer

    def get_queryset(self):

        teamid = self.request.query_params.get('teamid', None)
        teamcoach = Player.objects.all()[1].team.teamcoach

        if teamcoach == self.request.user or self.request.user.is_superuser:
            return Player.objects.filter(team__id=teamid)
        else:
            raise ValidationError(
                "Only the respective coach or admin user can view the players details!")


# Functionality:  get the personal details of the given user
# to access the details user must have logged into the system
# details can be accessible only by an admin user or the coach of their team


class PlayerPersonalDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayersPersonalDetailsListSerializer
    permission_classes = [TeamCoachOrAdmin]


# Functionality:  find the players who are laid in the 90th percentile
# to access the details user must have logged into the system
# details can be accessible only by an admin user or the coach of their team


class FindnintyPercentilePlayers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teamid = self.request.query_params.get('id', None)
        teamcoach = Player.objects.all()[1].team.teamcoach
        print(teamcoach)
        # filter the players based on the requested team using the passed query parameter
        queryset = Player.objects.filter(team=teamid)
        # using serializer take only the required fields from the database
        serializer = NintyPercentilePlayersListSerializer(queryset, many=True)
        result = JSONRenderer().render(serializer.data)
        # find the players who are laid in the 90th percentile
        percentiledPlayers = Calculate.calculatePercentile(json.loads(result))

        if teamcoach == self.request.user or self.request.user.is_superuser:
            return Response(percentiledPlayers, status=status.HTTP_200_OK)
        else:
            raise ValidationError(
                "Only the respective coach or admin user can view the players details!")
