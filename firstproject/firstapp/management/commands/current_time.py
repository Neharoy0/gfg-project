from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

from django.utils import timezone

class Command(BaseCommand):
    help = "Create a normal user"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **kwargs):
       print(timezone.now())