from django.db import models
from teams.models import Team


class Player(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=70)
    heights = models.IntegerField()
    averagescore = models.DecimalField(max_digits=4, decimal_places=2)
    numberofgamesplayed = models.IntegerField()

    def __str__(self):
        return self.name
