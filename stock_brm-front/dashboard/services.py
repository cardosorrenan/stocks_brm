from cgitb import reset
import os, requests
from datetime import datetime, timedelta

from dashboard.client import Client

client = Client()

    
class APIStockBRMService:
    DOMAIN_NAME = 'http://localhost:8005/api/dashboard'
        
    def get_rates(self, query_params={}):
        response = client.get(self.DOMAIN_NAME + '/rate', 
                              query_params=query_params)
        data = response.json()
        return data['result']

    def persist_rates(self, payload={}):
        response = client.post(self.DOMAIN_NAME + '/rate', 
                               payload=payload)
        return response.json()
        
   
        
