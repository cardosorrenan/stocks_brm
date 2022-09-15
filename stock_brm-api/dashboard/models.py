from django.db import models

from datetime import datetime

class Currency(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False, null=False, verbose_name='Name')
    symbol = models.CharField(max_length=1, unique=True, blank=False, null=False, verbose_name='Symbol')
    short = models.CharField(max_length=3, unique=True, blank=False, null=False, verbose_name='Short')

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return f'{self.name} ({self.short})'


class Date(models.Model):
    date = models.DateTimeField(unique=True, blank=False, null=False, verbose_name='Date')
    date_currency_rate = models.ManyToManyField(Currency, through='RatesUSD')
    
    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'

    def __str__(self):
        return self.date


class RatesUSD(models.Model):
    date = models.ForeignKey(Date, on_delete=models.PROTECT, blank=False, null=False, related_name='usd_rates', verbose_name='Date')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, blank=False, null=False, related_name='usd_rates', verbose_name='Currency')
    rate = models.DecimalField(decimal_places=16, max_digits=32, blank=False, null=False, verbose_name='Rate')
    
    class Meta:
        verbose_name = 'Rate USD'
        verbose_name_plural = 'Rates USD'

    def __str__(self):
        return f'{self.currency.short} in {datetime.strftime(self.date.date, "%d-%m-%Y")}'
    