from django.core.management.base import BaseCommand, CommandError

from partner.models import Client

class ClientCommand(BaseCommand):
    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError('need exactly zero arguments')

        for i in range(3000):
            Client(number=i).save()