import requests


class Client():
    
    def get(self, url, query_params=None):
        try:
            return requests.get(url, params=query_params)
        except requests.exceptions.ConnectionError as err:
            print(err)
        
    def post(self, url, payload=None):
        try:
            return requests.post(url, data=payload)
        except requests.exceptions.ConnectionError as err:
            print(err)