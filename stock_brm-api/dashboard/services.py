import os

from dashboard.client import Client

client = Client()


class VatComplyService():
    #DOMAIN_NAME = os.environ.get('DOMAIN_NAME_VATCOMPLY_SERVICE')
    DOMAIN_NAME = 'https://api.vatcomply.com'
    
    def get_rate_currency_usd(self, params=dict()):
        ENDPOINT = '/rates'
        params = {'base': 'USD', **params}
        return client.get(self.DOMAIN_NAME + ENDPOINT, params=params)