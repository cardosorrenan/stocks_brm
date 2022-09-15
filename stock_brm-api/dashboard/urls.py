from django.urls import path

from dashboard.views import ChartRateUSD


urlpatterns = [
    path('chartrateusd', ChartRateUSD.as_view(), name='chart_rate_usd'),
]