"""
This file provides ModelSerializer classes that are used for all views concerning Currency in Wutiko Locationsapp Application.
These Serializers classes are used to converting our Django Model Instances to JSON format so that they can be human readable.
We have simple model and nested serializers to as a representation of the desired fields to be displayed on our API FORMS
"""

from rest_framework import serializers
from .models import Currency, CurrencyRate


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = "__all__"
