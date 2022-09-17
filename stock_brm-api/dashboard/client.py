import requests


class Client():
    
    def get(self, url, params=None):
        response = requests.get(url, params=params)
        data = response.json()
        return { 'result': data }

