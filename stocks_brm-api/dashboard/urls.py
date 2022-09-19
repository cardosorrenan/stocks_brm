from django.urls import path

from dashboard.views import RateAPIView


urlpatterns = [
    path('rate', RateAPIView.as_view(), name='rate'),
]