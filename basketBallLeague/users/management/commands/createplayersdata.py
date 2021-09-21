from django.core.management.base import BaseCommand
from faker import Faker
from users.models import Player
from teams.models import Team
import faker.providers
import random

# team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     name = models.CharField(max_length=70)
#     heights = models.IntegerField()
#     averagescore = models.DecimalField(max_digits=4, decimal_places=2)
#     numberofgamesplayed = models.IntegerField()


class Command(BaseCommand):
    help = "Commad Information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        i = 0
        for _ in range(160):
            if(i == 16):
                i = 0
            Player.objects.create(
                team=Team.objects.all()[i],
                name=fake.name(),
                heights=round(random.uniform(150, 170)),
                averagescore=round(random.uniform(50.99, 99.99), 2),
                numberofgamesplayed=round(random.uniform(3, 6))
            )
            i = i+1
        print("Players data inserted successfully")
