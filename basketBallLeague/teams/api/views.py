from teams.models import Team
from teams.api.serializers import TeamListSerializer
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from teams.api.permissions import TeamCoachOrAdmin


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


# Functionality: get team detail by id
# along with the team details result includes list of players with their personal details
# to access the details user must have logged into the system as an admin user or the coach of their team
class TeamDetail(generics.RetrieveAPIView):
    permission_classes = [TeamCoachOrAdmin]
    queryset = Team.objects.all()
    serializer_class = TeamListSerializer
