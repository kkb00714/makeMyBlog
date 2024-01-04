from django.contrib import admin
from django.urls import path, include

from myBlog.views import BlogList, PostCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('main/', BlogList.as_view(), name='blog-list'),
    path('main/create/', PostCreate.as_view(), name='post-create'),
    
]
