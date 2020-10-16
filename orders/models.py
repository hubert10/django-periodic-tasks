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
    title = models.CharField(max_length=200, )
    description = models.CharField(max_length=500, )

    def __str__(self):
        return f"Product: {self.title}"


class Order(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, )
    confirmed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order: {self.id} - product: {self.product.title}"

    class Meta:
        ordering = ["-added"]


class Currency(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	currency_label = models.CharField(max_length=255, null=True)
	currency_name = models.CharField(max_length=255, null=True)
	is_active = models.BooleanField(default=True)


	def __str__(self):
		return self.currency_name + ' (' + self.currency_label + ')'

	class Meta:
		ordering = ('currency_name',)
		verbose_name = _('Currency')
		verbose_name_plural = _('Currencies')


class CurrencyRate(models.Model):
	class Permanent:
		# If you need to restore a deleted object instead of re-creating the same one use the restore_on_create attribute:
		restore_on_create = True
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
	currency_label = models.CharField(max_length=255, null=True)
	currency_rate = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.currency_label
	
	class Meta:
		ordering = ('currency_label',)
		verbose_name = _('Currency Rate')
		verbose_name_plural = _('Currency Rates')