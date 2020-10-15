from datetime import timedelta, time, datetime
from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from django.shortcuts import render
from django.views.generic import ListView
from django.conf import settings
from orders.models import Order, Product, Currency, CurrencyRate
from orders.serializers import CurrencyRateSerializer
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

        if len(Currency.objects.all()) == 0:
            respons = urllib.request.urlopen(settings.OPEN_EXCHANGERATES_URL)
            htm = respons.read().decode("utf-8")
            my_dicti = json.loads(htm)
            for k, v in my_dicti.items():
                Currency.objects.get_or_create(
                    currency_label=str(k), currency_name=str(v)
                )
        try:
            respon = urllib.request.urlopen(settings.OPEN_EXCHANGERATES_LATEST_URL)
            html = respon.read().decode("utf-8")
            my_dictio = json.loads(html)
            my_dictio = my_dictio["rates"]
            for k, v in my_dictio.items():
                obj, created = CurrencyRate.objects.get_or_create(currency_label=str(k))
                if created:
                    ab = CurrencyRate.objects.get(currency_label=str(k))
                    ab.currency_rate = str(v)
                    ab.save()
                else:
                    obj.currency_rate = str(v)
                    obj.save()
        except Exception:
            pass
        self.stdout.write("Currencies Successfully Updated.")
