from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=75)
    averagescore = models.DecimalField(max_digits=4, decimal_places=2)
    teamcoach = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
