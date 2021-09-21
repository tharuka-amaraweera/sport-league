from django.core.management.base import BaseCommand
from faker import Faker
from users.models import Coach
from teams.models import Team


class Command(BaseCommand):
    help = "Commad Information"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for i in range(16):
            Coach.objects.create(
                team=Team.objects.all()[i],
                name=fake.name()
            )
        print("Coaches data inserted successfully")
