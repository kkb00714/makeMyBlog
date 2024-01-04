from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from .models import Post, Comment
from .serializer import BlogBaseModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics

# 데이터를 처리

# 1. 게시판 조회기능
class BlogList(generics.ListAPIView):

    queryset = Post.objects.all()
    # queryset => Post 객체를 가져와 queryset에 할당
    
    serializer_class = BlogBaseModel
    # generics.ListAPIView가 기본적으로 get 메서드에서 
    # queryset을 가져와 직렬화한 결괏값을 반환

    template_name = 'blog_list.html'
    

        
        
        

        
        
    

        
        
# 2. 게시글 생성 기능


# 3. 게시글 업데이트 기능


# 4. 게시글 삭제 기능

