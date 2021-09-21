from rest_framework import serializers

from teams.models import Team
from users.api.serializers import PlayerListSerializer


# Functionality:
# view all team details with theiraverage scores and it's list of players with their details
class TeamListSerializer(serializers.ModelSerializer):
    # use nested serializer to add related players as an another field to the team serializer
    players = PlayerListSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = "__all__"
