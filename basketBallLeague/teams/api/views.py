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
from rest_framework.permissions import IsAuthenticated


# Functionality: get all team details
# along with the team details result includes list of players with their personal details
# to access the details user must have logged into the system as an admin user

class TeamList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeamListSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Team.objects.all()
        else:
            raise ValidationError(
                "Only the respective coach or admin user can view the players details!")


# get team detail by id
class TeamDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
