import os
import csv

from django.core.management.base import BaseCommand
from django.db import transaction

from rates.models import Currency

class Command(BaseCommand):
    help = 'Load currencies and stores them in the database'

    def handle(self, *args, **options):

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'currencies.csv')) as f:

            reader = csv.DictReader(f, skipinitialspace=True)

            with transaction.atomic():

                for row in reader:
                    print('Adding currency record for %(country_name)s' % row)
                    c = Currency(**row)
                    c.save()
