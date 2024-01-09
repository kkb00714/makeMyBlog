from django.contrib import admin
from django.urls import path

from myBlog.views import (PostDetail, 
                        PostList,
                        CommentCreate,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 게시글 url
    path('main/', PostList.as_view(), name='post-list'),
    path('main/detail/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    path('comments/', CommentCreate.as_view(), name='comment'),
]
