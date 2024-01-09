from django.contrib import admin
from django.urls import path

from myBlog.views import (PostDetail, 
                        PostList,
                        CommentCreate,
                        CommentDelete,
                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 게시글 url
    path('main/', PostList.as_view(), name='post-list'),
    path('main/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    path('main/<int:post_id>/comment', CommentCreate.as_view(), name='comment-create'),
    path('main/<int:post_id>/comment/<int:comment_id>', CommentDelete.as_view(), name='comment-delete'),
]
