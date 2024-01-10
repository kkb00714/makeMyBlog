from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse

from django.contrib.auth.models import User
from .models import Post, Comment
from .serializer import (
                        BlogBaseModel,
                        PostCreateModel,
                        PostDetailModel,
                        PostUpdateModel,
                        CommentCreateModel,
                        CommentDeleteModel,
                        BaseCommentModel,
                        )

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
    serializer_class = PostDetailModel
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# 3. 댓글 작성(생성) 기능
class CommentCreate(generics.CreateAPIView):
    serializer_class = BaseCommentModel

    def perform_create(self, serializer):
        serializer.save()
        
        post_serializer = PostCreateModel(serializer.instance.post)
        post_data = post_serializer.data
        return JsonResponse(post_data, safe=False)

# 4. 댓글 삭제 기능
class CommentDelete(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteModel
    lookup_url_kwarg = 'comment_id'

    def destroy(self, request, *args, **kwargs):
        # URL에서 댓글 ID 추출
        comment_id = self.kwargs.get('comment_id')

        
        comment_instance = self.get_object()        
        # 댓글 삭제 후 게시글 화면으로 리다이렉션
        
        post_id = comment_instance.post.id
        comment_instance.delete()
    
        return Response(status=status.HTTP_200_OK)