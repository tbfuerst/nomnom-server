from django.core.management.base import BaseCommand, CommandError

from nomnom.models import Ingredient


class Command(BaseCommand):
    help = 'Creates mock data and fills database with it.'

    def handle(self, *args, **options):
        Recipe.objects.all().delete()
