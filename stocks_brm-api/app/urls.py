from django.contrib import admin
from django.urls import path, include

from app import yasg_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dashboard/', include('dashboard.urls')),
]

urlpatterns += yasg_schema.urls