from django.db import models
from teams.models import Team

# Create your models here.


class Game(models.Model):
    teamwon = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.CharField(max_length=50)
    finalscore = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.game
