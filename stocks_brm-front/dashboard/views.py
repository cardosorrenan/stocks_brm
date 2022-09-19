from django.shortcuts import render
from django.views.generic import TemplateView

from dashboard.services import APIStocksBRMService
from dashboard.utils import CreateContext


service = APIStocksBRMService()

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get(self, request, *args, **kwargs):
        context = CreateContext(request=request)
        return render(request, self.template_name, context.get_context())
    
    def post(self, request, *args, **kwargs):
        context = CreateContext(request=request)
        try:
            start, end = context.get_formatted_date('%d-%m-%Y')
            payload = {
                'start': start,
                'end': end,
                'currency_from': request.POST.get('currency_from'),
            }
            service.persist_rates(payload=payload)
            
            query_params = {
                **payload,
                'currency_to': request.POST.get('currency_to'),
            }
            context.rates = service.get_rates(query_params=query_params)
        except Exception as err:
            print(err)
        return render(request, self.template_name, context.get_context())