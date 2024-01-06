from django.shortcuts import render
from django.http import Http404

from django.contrib.auth.models import User
from .models import Post, Comment
from .serializer import (
                        BlogBaseModel,
                        PostCreateModel,
                        PostDetailModel,
                        PostUpdateModel,
                        PostDeleteModel,
                        )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics
from rest_framework import status

# 데이터를 처리

# 1. 게시글 조회 (게시글 상세)
class PostDetail(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    # queryset => Post 객체를 가져와 queryset에 할당
    
    serializer_class = BlogBaseModel
    # generics.ListAPIView가 기본적으로 get 메서드에서 
    # queryset을 가져와 직렬화한 결괏값을 반환

    template_name = 'blog_detail.html'
    
# 2. 게시글 생성
class PostCreate(generics.CreateAPIView):
    
    queryset = Post.objects.all()    
    serializer_class = BlogBaseModel
    # template_name = 'post_create.html'

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


# 3. 게시글 업데이트 기능
class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()    
    serializer_class = BlogBaseModel
    # template_name = 'post_update.html'
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # 업데이트할 대상 객체인 instance에
        # data = request.data (클라이언트로부터 받은 새로운 데이터) 를 담음
        # partial = True 는 부분 업데이트를 허용한다는 옵션.

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # 실제 업데이트를 수행
        
        return Response(serializer.data)

# 4. 게시글 삭제 기능
class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()    
    serializer_class = BlogBaseModel
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    