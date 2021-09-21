from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
import random
from games.models import Game
from teams.models import Team

# sample data for games
TOURNAMENT = ["tournament 1", "tournament 2", "tournament 3", "tournament 4", "tournament 5", "tournament 6",
              "tournament 7", "tournament 8", "tournament 9", "tournament 10", "tournament 11", "tournament 12",
              "tournament 13", "tournament 14", "tournament 15", "tournament 16", "tournament 17", "tournament 18",
              "tournament 19", "tournament 20", "tournament 21", "tournament 22", "tournament 23", "tournament 24",
              "tournament 25", "tournament 26", "tournament 27", "tournament 28", "tournament 29", "tournament 30",
              "tournament 31" "tournament 32"]


class Provider(faker.providers.BaseProvider):
    def tournament_name(self):
        return self.random_element(TOURNAMENT)


class Command(BaseCommand):
    help = "Commad Information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)
        for _ in range(len(TOURNAMENT)):
            g = fake.unique.tournament_name()
            Game.objects.create(
                teamwon=Team.objects.order_by('?').first(),
                game=g,
                finalscore=round(random.uniform(50.99, 99.99), 2)

            )
        print("Games data inserted successfully")
