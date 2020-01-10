from django.core.management.base import BaseCommand, CommandError

from nomnom.models import Tag_Category, Tag

from random_words import RandomWords
from datetime import date
from random import *
import random as rnd

# dirty seeder


class Command(BaseCommand):
    help = 'Creates mock data and fills database with it.'

    def handle(self, *args, **options):

        def rword(count, separator):
            rand = RandomWords()
            r = rand.random_words(count=count)
            words = separator.join(r)
            return words

        def rfloat():
            return (random()*1000).__round__(2)

        def rint():
            return int((random()*2000).__round__(0))

        def get_rnd_date(year):
            start_dt = date.today().replace(day=1, month=1).toordinal()
            end_dt = date.today().replace(day=31, month=12).toordinal()
            random_days = rnd.randint(start_dt, end_dt)
            if (random_days == 737484): #handle Feb 29
                random_days = 737483
            rnd_date = date.fromordinal(random_days)
            rnd_date.replace(year=year)
            return rnd_date

        def rints(count, separator):
            numbers = []
            for i in range(count):
                rng = int(random()*32000)
                strrng = str(rng)
                numbers.append(strrng)
            concat_numbers = separator.join(numbers)
            return concat_numbers

        def tag_categories():
            Tag_Category.objects.all().delete()
            for i in range(10):
                tagC = Tag_Category(name=rword(1,""))
                tagC.save()
            
        def tags():
            Tag.objects.all().delete()
            tagCs = Tag_Category.objects.all()

            def get_random_tag_cat():
                tagCat = tagCs[int((random()*9).__round__(0))]
                return tagCat

            for i in range (100):
                tagC = get_random_tag_cat()
                tag = Tag(name=rword(1,""), category=tagC)
                tag.save()


        # def account_template():
        #     Account_Template.objects.all().delete()

        #     att = Account_Type_Template.objects.all()
        #     att0 = att[0]
        #     ids = att[0].account_type_ids
        #     arrids = ids.split(';')

        #     ratt = []
        #     for i in range(30):
        #         randomid = arrids[int((random()*5).__round__(0))]
        #         ratt.append(randomid)

        #     strratt = ';'.join(ratt)

        #     acc = Account_Template(template_identifier=rword(2, ''), account_numbers=rints(
        #         30, ';'), type_template=att0, account_names=rword(30, ';'), account_descriptions=rword(30, ';'), type_ids=strratt)
        #     acc.save()

        # def account_type():
        #     Account_Type.objects.all().delete()
        #     for i in range(6):
        #         acc = Account_Type(type_id=rint(), name=rword(
        #             1, ''), description=rword(2, ' '))
        #         acc.save()

        # def account():
        #     Account.objects.all().delete()
        #     accountTypes = Account_Type.objects.all()

        #     def get_random_account():
        #         racc = accountTypes[int((random()*5).__round__(0))]
        #         return racc

        #     for i in range(45):
        #         racc = get_random_account()
        #         acc = Account(number=rint(), name=rword(2, ';'), description=rword(
        #             4, ' '), type_id=racc, is_deleted=False)
        #         acc.save()

        # def area():
        #     Area.objects.all().delete()
        #     for i in range(4):
        #         area = Area(name=rword(1,
        #                                ''), description=rword(5, ' '))
        #         area.save()

        # def transaction_tag():
        #     Transaction_Tag.objects.all().delete()
        #     for i in range(25):
        #         tag = Transaction_Tag(name=rword(1, ''))
        #         tag.save()

        # def transaction():

        #     Transaction.objects.all().delete()
        #     areas = Area.objects.all()
        #     accounts = Account.objects.all()
        #     tags = Transaction_Tag.objects.all()

        #     def get_rnd_account():
        #         racc = accounts[int((random()*5).__round__(0))]
        #         return racc

        #     def get_rnd_area():
        #         area = areas[int((random()*3).__round__(0))]
        #         return area

        #     def get_rnd_tags():
        #         tag = tags[int((random()*24).__round__(0))]
        #         return tag

        #     print("seeding transactions....")
        #     for i in range(transactions_count):
        #         created_at = get_rnd_date(2019)
        #         updated_at = get_rnd_date(2020)
        #         book_date = get_rnd_date(2020)
        #         stack_id = rint()
        #         area = get_rnd_area()
        #         account_id = get_rnd_account()
        #         c_account_id = get_rnd_account()
        #         description = rword(7, ' ')
        #         amount = rfloat()
        #         # TODO Add many to many tags as test
        #         transaction = Transaction(created_at=created_at, updated_at=updated_at, book_date=book_date, stack_id=stack_id,
        #                                   area=area, account_id=account_id, c_account_id=c_account_id, description=description, amount=amount)
        #         transaction.save()

        #     print("assigning transaction tags...")
        #     all_transac = Transaction.objects.all()

        #     def assign_rnd_tags():
        #         for i in range(transactions_count):
        #             transac = all_transac[i]
        #             rnd_tag_amount = int((random()*2).__round__(0))
        #             for j in range(rnd_tag_amount):
        #                 tag = get_rnd_tags()
        #                 transac.tags.add(tag)
        #             transac.save()
        #     assign_rnd_tags()
        #     print("transaction tags assigned")

        print("Seeding Tag Categories")
        tag_categories()
        print("Seeding Tags")
        tags()

        print("Seeding successful")