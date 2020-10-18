from django.shortcuts import render
from django.views.generic import ListView
from .models import Order, Product
from django.conf import settings
from .models import Order, Product, Currency, CurrencyRate
from .serializers import CurrencyRateSerializer
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


class OrderListView(ListView):
    model = Order



