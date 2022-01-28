from django.core.management.base import BaseCommand, CommandError

from partner.models import LegalEntity

class LegalCommand(BaseCommand):
    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError('need exactly zero arguments')

        for i in range(200):
            LegalEntity(number=i).save()