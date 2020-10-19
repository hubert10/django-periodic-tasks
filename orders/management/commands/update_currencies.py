from datetime import timedelta, time, datetime
from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
from orders.models import Order, Product, Currency, CurrencyRate
import django
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import *
from django.utils.translation import ugettext_lazy as _
import urllib, json
from django.http import HttpResponse


today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))


class Command(BaseCommand):
    help = "Updates Currecy Rates from  OpenExchange API"

    def handle(self, *args, **options):
        data = urllib.request.urlopen(settings.open_exchangerate_uri)
        html = data.read().decode("utf-8")
        data_dict = json.loads(html)
        data_dict = data_dict["rates"]
        for key, value in data_dict.items():
            obj, created = CurrencyRate.objects.get_or_create(label=str(key))
            if created:
                ab = CurrencyRate.objects.get(label=str(key))
                ab.rate = str(value)
                ab.save()
            else:
                obj.rate = str(value)
                obj.save()
        self.stdout.write("Currencies Successfully Updated.")
