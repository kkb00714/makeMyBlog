from django.shortcuts import render, get_object_or_404
from django.http import Http404


from django.contrib.auth.models import User
from .models import Post, Comment
from .serializer import (
                        BlogBaseModel,
                        PostCreateModel,
                        PostUpdateModel,
                        CommentCreateModel,
                        )

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

# 데이터를 처리

# 1. 게시글 목록 + 생성
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateModel
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # request로부터 받은 데이터를 기반으로 직렬화된 데이터 생성
        serializer.is_valid(raise_exception=True)
        # 받은 데이터 serializer의 유효성 검사를 하고 유효한 경우에만 .save() 호출
        instance = serializer.save(writer = request.user)
        # 직렬화된 데이터를 기반으로 모델 객체를 생성하고 저장
        
        headers = self.get_success_headers(serializer.data)
        # 응답 헤더를 가져옴. 주로 redirect 등의 추가 동작을 지원
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # 성공 응답 반환

# 2. 게시글 상세, 수정, 삭제
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    # queryset => Post 객체를 가져와 queryset에 할당
    serializer_class = PostUpdateModel
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
    

# 5. 댓글 작성(생성) 기능
class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentCreateModel
    
# 
