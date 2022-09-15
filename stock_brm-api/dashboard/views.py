from datetime import datetime, timedelta, timezone

from django.db import IntegrityError, transaction
from rest_framework.views import APIView
from rest_framework.response import Response

from dashboard.models import Currency, Date, RatesUSD
from dashboard.services import VatComplyService


class ChartRateUSD(APIView):
    service = VatComplyService()        
    
    def post(self, request):
        start = request.data.get('start', None)
        end = request.data.get('end', None)
        
        if None in (start, end):
            return Response({'message': 'The period needs to be provided.'}, 400)
        
        start = datetime.strptime(start, "%d-%m-%Y")
        end = datetime.strptime(end, "%d-%m-%Y")
        dates = [start + timedelta(days=x) for x in range(0, (end-start).days)]
        
        if not dates:
            return Response({'message': 'Max period = 5 days.'}, 400)
    
        if (dates[-1] - dates[0]).days > 4:
            return Response({'message': ''}, 400)       

        currencies = Currency.objects.exclude(short="USD")

        for date in dates:
            date_client = datetime.strftime(date, "%Y-%m-%d")  
                        
            rates = self.service.get_rate_currency_usd(params={"date": date_client})
            date_service = datetime \
                .strptime(rates['result']['date'], "%Y-%m-%d") \
                .replace(hour=14, minute=00, second=00, tzinfo=timezone.utc)
            
            try:
                with transaction.atomic():
                    if date_service.weekday() in [4, 5]:
                        date_service = datetime \
                            .strptime(date_client, "%Y-%m-%d") \
                            .replace(hour=14, minute=00, second=00, tzinfo=timezone.utc)
                    date_instance = Date(date=date_service)
                    date_instance.save()
                    for currency in currencies.iterator():                        
                        short = currency.short
                        rate = rates['result']['rates'][short]
                        date_instance.date_currency_rate.add(
                            currency, 
                            through_defaults={'rate': rate})
            except IntegrityError as error:
                print(date_client, error)
                
        return Response({'message': 'Success'} , 201)
        