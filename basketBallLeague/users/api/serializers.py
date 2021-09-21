from rest_framework import serializers
from users.models import Player


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class PlayersScoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "name", "averagescore"]


class PlayersPersonalDetailsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "name", "heights", "numberofgamesplayed"]


class NintyPercentilePlayersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "name", "averagescore", "team"]
