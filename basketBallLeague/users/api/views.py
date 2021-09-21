from rest_framework.response import Response
from users.models import Player
from users.api.serializers import (PlayerListSerializer, PlayersScoreListSerializer,
                                   PlayersPersonalDetailsListSerializer, NintyPercentilePlayersListSerializer)
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.renderers import JSONRenderer
import json
from users.api.datacalculations import Calculate


# get all team details


class PlayerList(generics.ListAPIView):
    serializer_class = PlayerListSerializer

    def get_queryset(self):
        return Player.objects.all()


# get player detail by id


class PlayerDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerListSerializer


# get list of players with their average scores


class PlayerScoreList(generics.ListAPIView):
    serializer_class = PlayersScoreListSerializer

    def get_queryset(self):
        return Player.objects.all()


# get personal details of selected player


class PlayerPersonalDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayersPersonalDetailsListSerializer


class FindnintyPercentilePlayers(APIView):
    def get(self, request):
        teamid = self.request.query_params.get('id', None)
        # filter the players based on the requested team using the passed query parameter
        queryset = Player.objects.filter(team=teamid)
        # using serializer take only the required fields from the database
        serializer = NintyPercentilePlayersListSerializer(queryset, many=True)
        result = JSONRenderer().render(serializer.data)
        # find the players who are laid in the 90th percentile
        percentiledPlayers = Calculate.calculatePercentile(json.loads(result))
        return Response(percentiledPlayers, status=status.HTTP_200_OK)
