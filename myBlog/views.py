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

    def get(self, request):
        blogs = Post.objects.all()
        # blogs => Post 객체를 가져와 blogs에 할당
        serializer = BlogBaseModel

        
        
    

        
        
# 2. 게시글 생성 기능


# 3. 게시글 업데이트 기능


# 4. 게시글 삭제 기능

