from django.contrib import admin
from django.urls import path, include

from myBlog.views import PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('main/detail/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('main/create/', PostCreate.as_view(), name='post-create'),
    path('main/update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('main/delete/<int:pk>', PostDelete.as_view(), name='post-delete'),

]
