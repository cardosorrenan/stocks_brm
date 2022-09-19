from datetime import datetime, timedelta


class CreateContext():
    
    def __init__(self, request=None):
        HTTP_METHOD = request.method
        if HTTP_METHOD == 'GET':
            self.end = datetime.today()
            if (self.end.hour < 11):
                self.end = self.end - timedelta(days=1)
            self.start = self.end - timedelta(days=4)
        elif HTTP_METHOD == 'POST':
            daterange = request.POST.get('daterange').split('-')
            self.start = datetime.strptime(daterange[0], '%d/%m/%Y')
            self.end =  datetime.strptime(daterange[1],'%d/%m/%Y')
        self.rates = []

    def get_formatted_date(self, format):
        return (self.start.strftime(format),
                self.end.strftime(format))

    def get_context(self):
        start, end = self.get_formatted_date('%d-%m-%Y')
        return {
            "start": start,
            "end": end,
            "rates": self.rates,
        }