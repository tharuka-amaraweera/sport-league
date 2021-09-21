from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

USERNAMES = [
    "AdamsBaker", "ClarkDavis", "EvansFrank", "GhoshHills", "IrwinJones",
    "KleinLopez", "MasonNalty", "OchoaPatel", "QuinnReily", "TrottSmith",
    "JamesRobert", "JohnMichael", "WilliamRichard", "JosephCharles", "ThomasChristopher",
    "DanielMatthew"
]
PASSWORD = [
    "AdamsBaker1234", "ClarkDavis1234", "EvansFrank1234", "GhoshHills1234", "IrwinJones1234",
    "KleinLopez1234", "MasonNalty1234", "OchoaPatel1234", "QuinnReily1234", "TrottSmith1234",
    "JamesRobert1234", "JohnMichael1234", "WilliamRichard1234", "JosephCharles1234", "ThomasChristopher1234",
    "DanielMatthew1234"
]
EMAIL = [
    "AdamsBaker@gmail.com", "ClarkDavis@gmail.com", "EvansFrank@gmail.com", "GhoshHills@gmail.com", "IrwinJones@gmail.com",
    "KleinLopez@gmail.com", "MasonNalty@gmail.com", "OchoaPatel@gmail.com", "QuinnReily@gmail.com", "TrottSmith@gmail.com",
    "JamesRobert@gmail.com", "JohnMichael@gmail.com", "WilliamRichard@gmail.com", "JosephCharles@gmail.com", "ThomasChristopher@gmail.com",
    "DanielMatthew@gmail.com"
]


class Command(BaseCommand):
    help = "Commad Information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        User.objects.create(
            username="adminuser",
            password="admin1234",
            email="admin@gmail.com",
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        print("Admin user created")

        for i in range(16):

            User.objects.create(
                username=USERNAMES[i],
                password=PASSWORD[i],
                email=EMAIL[i],
                is_active=True
            )
        print("Coches created")
