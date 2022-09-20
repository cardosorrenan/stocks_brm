import pytest
from datetime import datetime, timezone

from rest_framework.test import APIClient

from dashboard.models import Currency

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def create_currency():
    currency = Currency(name="US Dollar",
                        symbol="$",
                        short="USD",
                        created_at=datetime.now(tz=timezone.utc))
    currency.save()
    
@pytest.fixture
def rate_params():
    query = dict()
    query['currency_from'] = 'USD';
    query['currency_to'] = 'BRL';
    query['start'] = '15-09-2022';
    query['end'] = '19-09-2022';
    return query