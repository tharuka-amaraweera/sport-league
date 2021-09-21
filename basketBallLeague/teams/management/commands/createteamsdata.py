from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from teams.models import Team
import random

# sample team name
TEAMS = [
    "Matadors", "Defenders", "Shooting Stars", "Shockers", "Jazz Gaming", "Jayhawks", "Kings Guard Gaming",
    "Bucks Gaming", "Fast & the Furious", "Panthers", "Out of the Ordinary", "Grasshoppers", "River Hawks",
    "Aardvarks", "Seminoles", "The Crossovers"
]


class Provider(faker.providers.BaseProvider):
    def team_names(self):
        return self.random_element(TEAMS)


class Command(BaseCommand):
    help = "command information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(Provider)
        for _ in range(16):
            t = fake.unique.team_names()
            Team.objects.create(
                name=t,
                averagescore=round(random.uniform(50.99, 99.99), 2)
            )
        print("Teams data inserted successfully")
