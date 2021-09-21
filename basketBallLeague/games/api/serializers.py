from rest_framework import fields, serializers

from games.models import Game

# Functionality:
# view all games with their final scores


class GameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
