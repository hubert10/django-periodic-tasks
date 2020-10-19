import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=200,
    )
    description = models.CharField(
        max_length=500,
    )

    def __str__(self):
        return f"Product: {self.title}"


class Order(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    confirmed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order: {self.id} - product: {self.product.title}"

    class Meta:
        ordering = ["-added"]


class Currency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " (" + self.label + ")"

    class Meta:
        ordering = ("name",)


class CurrencyRate(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    label = models.CharField(max_length=25, null=True)
    rate = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ("label",)
