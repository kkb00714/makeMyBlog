from .models import Post, Comment
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.shortcuts import render, get_object_or_404, redirect

# 게시판 기본 설정
class BlogBaseModel(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [       
            'pk',
            'title', 
            'writer',
            'image',
            'content',
            'created_at',
            'modified_at',
            'view_count',
            ]
        
        # exclude = ['field_to_exclude']
        # 나중에 제외하고 싶은 필드 추가할 때 사용
        

# 댓글 기본 설정
class BaseCommentModel(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'pk',
            'post',
            'writer',
            'content',
            'created_at',
        ]
    
    def create(self, validated_data):
        post = validated_data.pop('post')  
        # post를 추출
        validated_data['post'] = post  
        # 추출한 post_id를 사용해 게시글 객체를 가져와서 저장
        return super().create(validated_data)


# 게시글 작성
class PostCreateModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        fields = [
            'pk',
            'title', 
            'writer',
            'image',
            'content',
            'created_at',
            'modified_at',
            ]

# 게시글 상세보기
class PostDetailModel(BlogBaseModel):
    comments = serializers.SerializerMethodField()
    
    def get_comments(self, instance):
        comments = Comment.objects.filter(post=instance)
        serializer = BaseCommentModel(comments, many=True)
        return serializer.data

    class Meta(BlogBaseModel.Meta):
        fields = [
                'pk',
                'title', 
                'writer', 
                'image', 
                'content', 
                'created_at', 
                'modified_at', 
                'view_count', 
                'comments',
                ]
        

# 게시글 업데이트
class PostUpdateModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        fields = [
            'title', 
            'content', 
            'image',
            ]

# 게시글 삭제
class PostDeleteModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        pass
    
        
# 댓글 생성
class CommentCreateModel(BaseCommentModel):
    class Meta(BaseCommentModel.Meta):
        fields = [
            'pk',
            'writer', 
            'content',
            'created_at'
            ]

# 댓글 업데이트 -> 삭제
# class CommentUpdateModel(BaseCommentModel):
#     class Meta(BaseCommentModel.Meta):
#         fields = ['content']

# 댓글 삭제
class CommentDeleteModel(BaseCommentModel):
    class Meta(BaseCommentModel.Meta):
        pass
    
    def destroy(self, instance):
        instance.delete()
    

