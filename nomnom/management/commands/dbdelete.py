from django.core.management.base import BaseCommand, CommandError

from accant.models import Account_Type_Template
from accant.models import Account_Template
from accant.models import Account_Type
from accant.models import Account
from accant.models import Area
from accant.models import Transaction
from accant.models import Transaction_Tag


class Command(BaseCommand):
    help = 'Creates mock data and fills database with it.'

    def handle(self, *args, **options):
        Account_Type_Template.objects.all().delete
        Account_Template.objects.all().delete
        Account_Type.objects.all().delete
        Account.objects.all().delete
        Area.objects.all().delete
        Transaction.objects.all().delete
        Transaction_Tag.objects.all().delete
