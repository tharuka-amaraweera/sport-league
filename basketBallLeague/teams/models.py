from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=75)
    averagescore = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name
