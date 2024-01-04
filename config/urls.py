from django.contrib import admin
from django.urls import path

from rest_framework import routers
# Router 사용 - API 엔드포인트 설정을 위해



urlpatterns = [
    path('admin/', admin.site.urls),
    
]
