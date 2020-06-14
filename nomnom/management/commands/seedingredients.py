from django.core.management.base import BaseCommand, CommandError
from nomnom.models import Ingredient

import csv
import sys
import pprint


class Command(BaseCommand):
    help = 'Creates mock data and fills database with it.'

    def handle(self, *args, **options):
        reader = csv.DictReader(
            open("/opt/app/nomnom/management/commands/Zutatenliste.csv", 'r'))
        dict_list = []
        for line in reader:
            dict_list.append(line)
        pprint.pprint(dict_list)

        for ingredient in dict_list:
            ingred = Ingredient(name=ingredient)
            ingred.save()
