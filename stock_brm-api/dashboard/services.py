from dashboard.client import Client

client = Client()


class VatComplyService():
    #DOMAIN_NAME = os.environ.get('DOMAIN_NAME_VATCOMPLY')
    DOMAIN_NAME = 'https://api.vatcomply.com'
    
    def get_rate(self, params={}):
        ENDPOINT = '/rates'
        return client.get(self.DOMAIN_NAME + ENDPOINT, params=params)