from django.contrib import admin
from django.urls import path, include

from myBlog.views import BlogList

from rest_framework import routers
# Router 사용 - API 엔드포인트 설정을 위해

router = routers.DefaultRouter()
router.register('posts', BlogList)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', BlogList.as_view(), name='blog-list'),

    
]
