import os, requests


class DashboardService():
    URL_API = os.environ.get('URL_API', '')
    
    def get(self, endpoint, params):
        url = self.URL_API + endpoint
        response = requests.get(url, params=params)
        data = response.json()
        return { 
            'result': data
        }
