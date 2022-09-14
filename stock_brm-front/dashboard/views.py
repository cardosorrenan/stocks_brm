from queue import Empty
from django.shortcuts import render
from django.views.generic import TemplateView

import datetime

from dashboard.services import DashboardService


dashboard_service = DashboardService()

# Create your views here.
class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get(self, request, *args, **kwargs):
        TIME_GMT_REFRESH = 11
   
        if len(request.GET):
            period = request.GET.get('date', '')
            start, end = period.split('_')
        else:    
            end = datetime.datetime.today()
            if (end.hour < TIME_GMT_REFRESH):
                end = start - datetime.timedelta(days=1)
            start = end - datetime.timedelta(days=5)
        rate = 'BRL'
        #params = {
        #    rate: rate,
        #    start: start,
        #    end: end,
        #}
        #data = dashboard_service.get('/chart_rate', params)
        data = {
            "result": [
                [1662732000, 115.36],
                [1662818400, 115.54],
                [1662904800, 112.13],
                [1662991200, 110.34],
                [1663077600, 106.84]
            ]
        }
        data = list(map(lambda d: [d[0]*1000 , d[1]], data['result']))
        
        context = dict()
        context['start'] = start.strftime('%d/%m/%Y')
        context['end'] = end.strftime('%d/%m/%Y')
        context['data'] = data
        return render(request, self.template_name, context)
    
    