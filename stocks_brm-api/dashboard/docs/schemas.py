from drf_yasg import openapi

schemas = {
    'rate': {
        'GET': [
            openapi.Parameter(
                'currency_from',
                in_=openapi.IN_QUERY,
                default='USD',
                type=openapi.TYPE_STRING,
                required=True),
            openapi.Parameter(
                'currency_to',
                in_=openapi.IN_QUERY,
                default='BRL',
                type=openapi.TYPE_STRING,
                required=True),
            openapi.Parameter(
                'start',
                in_=openapi.IN_QUERY,
                default='19-09-2022',
                type=openapi.TYPE_STRING,
                required=True),
            openapi.Parameter(
                'end',
                in_=openapi.IN_QUERY,
                default='23-09-2022',
                type=openapi.TYPE_STRING,
                required=True)
        ],
    }
}