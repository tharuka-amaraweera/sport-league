from rest_framework.response import Response
from teams.models import Team
from teams.api.serializers import TeamListSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# get all team details
class TeamList(generics.ListAPIView):
    serializer_class = TeamListSerializer

    def get_queryset(self):
        return Team.objects.all()


# get team detail by id
class TeamDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer

# get all team details in sorted order to reflect who won & competition progress


class TeamOrderedList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['averagescore']

    def get_queryset(self):
        return Team.objects.all()
