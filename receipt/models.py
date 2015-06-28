# coding=utf-8
from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal


# Create your models here.
class Receipt(models.Model):
	account = models.ForeignKey(settings.AUTH_USER_MODEL)
	date_created = models.DateTimeField(auto_now_add=True)
	prize_total = models.DecimalField(max_digits=10, decimal_places=2)
	cc_used = models.ForeignKey('businessquiz.CreditCard')

	class Meta:
		ordering = ('-pk',)

	def __unicode__(self):
		return 'Receipt #%d' % self.pk

	def save(self, *args, **kwargs):
		self.prize_total = self.get_prize_total_inkl_vat()
		return super(Receipt, self).save(*args, **kwargs)

	def get_vat(self):
		return self.get_prize_total_exkl_vat() * Decimal(0.25)

	def get_prize_total_exkl_vat(self):
		if Item.objects.filter(receipt=self).first():
			qs = Item.objects.filter(receipt=self).aggregate(Sum('prize_total'))
			prize_total = qs['prize_total__sum']
		else:
			prize_total = 0
		return prize_total

	def get_prize_total_inkl_vat(self):
		return self.get_prize_total_exkl_vat() + self.get_vat()


class Item(models.Model):
	receipt = models.ForeignKey(Receipt)
	name = models.CharField(max_length=256)
	amount = models.PositiveIntegerField()
	prize_each = models.DecimalField(max_digits=10, decimal_places=2)
	prize_total = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return '%d %s' % (self.amount, self.name)

	def save(self, *args, **kwargs):
		self.prize_total = self.amount * self.prize_each

		return super(Item, self).save(*args, **kwargs)
