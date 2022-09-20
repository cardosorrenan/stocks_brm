import pytest

from rest_framework import status

@pytest.mark.django_db
def test_rates_list(client, rate_params):
    response = client.get('/api/dashboard/rate', rate_params)
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('result', None) != None
    
@pytest.mark.django_db
def test_rates_create(client, rate_params, create_currency):
    del rate_params['currency_to']
    response = client.post('/api/dashboard/rate', rate_params)
    assert response.status_code == status.HTTP_201_CREATED
