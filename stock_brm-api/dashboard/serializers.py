from dashboard.models import Currency, Date
from rest_framework import serializers


class DateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Date
        fields =  ('id', 'date')
        
        
class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields =  ('id', 'name', 'symbol', 'short')