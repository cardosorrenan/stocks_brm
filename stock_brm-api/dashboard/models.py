from django.db import models

from datetime import datetime, timezone

class Currency(models.Model):
    name = models.CharField(max_length=128, 
                            unique=True, 
                            blank=False, 
                            null=False, 
                            verbose_name='Name')
    symbol = models.CharField(max_length=1,
                              unique=True,
                              blank=False,
                              null=False,
                              verbose_name='Symbol')
    short = models.CharField(max_length=3,
                             unique=True,
                             blank=False,
                             null=False,
                             verbose_name='Short')

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return f'{self.name} ({self.short})'


class Date(models.Model):
    date = models.DateTimeField(unique=True,
                                blank=False,
                                null=False,
                                verbose_name='Date')

    class Meta:
        verbose_name = 'Date'
        verbose_name_plural = 'Dates'

    def save(self, *args, **kwargs):
        self.date = (datetime
            .strptime(self.date, "%Y-%m-%d")
            .replace(hour=14, 
                     minute=00, 
                     second=00, 
                     tzinfo=timezone.utc))
        super(Date, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.date.strftime("%d/%m/%Y %H:%M:%S")
    
    def get_iso(self):
        return int(self.date.timestamp() * 1000)


class Rate(models.Model):   
    date = models.ForeignKey(Date,
                             on_delete=models.PROTECT,
                             blank=False,
                             null=False,
                             related_name='usd_rates',
                             verbose_name='Date')
    currency_from = models.ForeignKey(Currency,
                                      on_delete=models.PROTECT,
                                      blank=False,
                                      null=False,
                                      related_name='usd_rates_from',
                                      verbose_name='Currency Origin')
    currency_to = models.ForeignKey(Currency,
                                    on_delete=models.PROTECT,
                                    blank=False,
                                    null=False,
                                    related_name='usd_rates_to',
                                    verbose_name='Currency Destiny')
    rate = models.DecimalField(decimal_places=16,
                               max_digits=32,
                               blank=False,
                               null=False,
                               verbose_name='Rate')
    
    class Meta:
        unique_together = (('date', 'currency_from', 'currency_to'),)
        verbose_name = 'Rate'
        verbose_name_plural = 'Rates'

    def __str__(self):
        return f'{self.currency_from.short}->{self.currency_to.short} in {datetime.strftime(self.date.date, "%d-%m-%Y")}'