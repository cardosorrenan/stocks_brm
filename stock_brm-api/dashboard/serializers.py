from datetime import timedelta

from rest_framework import serializers

from dashboard.models import Rate

class RateInputSerializer(serializers.Serializer):
    start = serializers.DateField(input_formats=['%d-%m-%Y'])
    end = serializers.DateField(input_formats=['%d-%m-%Y'])    
    currency_from = serializers.CharField(max_length=3)
    currency_to = serializers.CharField(max_length=3)
    
    def validate(self, data):
        start = data['start']
        end = data['end']
        if (end - start).days > 4:
            raise serializers.ValidationError("Max Period = 5 days.")        
        if start > end:
            raise serializers.ValidationError("End date must occur after date start.")
        data['end'] = end + timedelta(days=1)
        return data


class CreateRateInputSerializer(RateInputSerializer):
    currency_to = serializers.CharField(max_length=3, required=False)


class RateOutputSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source='date.date')
    
    class Meta:
        model = Rate
        fields = ('date', 'rate',)

        
    def to_representation(self, instance):
        return (instance.date.get_iso(), instance.rate,)        
