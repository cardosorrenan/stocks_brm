from datetime import datetime, timedelta, timezone


from django.db.models import F
from django.db import IntegrityError, transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from dashboard.serializers import RateInputSerializer, RateOutputSerializer, CreateRateInputSerializer

from dashboard.models import Currency, Date, Rate
from dashboard.services import VatComplyService

service = VatComplyService()    

class RateAPIView(APIView):
    
    def get(self, request):
        query_params = request.query_params
        serializer = RateInputSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)
        start, end, curr_from, curr_to = serializer.validated_data.values()
        results = Rate.objects.filter(date__date__gte=start,
                                      date__date__lte=end, 
                                      currency_to__short=curr_to,
                                      currency_from__short=curr_from)
        results_serializer = RateOutputSerializer(results, many=True)
        response = { 'result': results_serializer.data }
        return Response(response, 200)
    

    def post(self, request):
        payload = request.data
        serializer = CreateRateInputSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        start, end, currency_from = serializer.validated_data.values()
        
        currencies = Currency.objects.all()
        currency_from = currencies.get(short=currency_from)
        currencies = currencies.exclude(short=currency_from.short)
        dates = [start + timedelta(days=x) for x in range(0, (end-start).days)]
        
        for date in dates:
            date = datetime.strftime(date, "%Y-%m-%d")  
            rates = service.get_rate({"date": date, "base": currency_from.short})
            try:
                with transaction.atomic():
                    date_instance = Date.objects.create(date=date)
                    for currency in currencies.iterator():
                        short = currency.short
                        Rate.objects.create(date=date_instance,
                                            currency_from=currency_from,
                                            currency_to=currencies.get(short=short),
                                            rate=rates['result']['rates'][short])
            except IntegrityError as error:
                print(date, error)

        return Response({'message': 'Success'} , 201)