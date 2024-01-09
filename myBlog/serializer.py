from .models import Post, Comment
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# 댓글 기본 설정
class BaseCommentModel(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'writer',
            'content',
            'created_at',
        ]

# 게시판 기본 설정
class BlogBaseModel(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [            
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
        
# 게시글 작성
class PostCreateModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        fields = [
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
    
    class Meta(BlogBaseModel.Meta):
        fields = [
                'id', 
                'title', 
                'writer', 
                'image', 
                'content', 
                'created_at', 
                'modified_at', 
                'view_count', 
                'comments',
                ]
        
    def get_comments(self, instance):
        comments = Comment.objects.filter(post=instance)
        serializer = BaseCommentModel(comments, many=True)
        return serializer.data

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
            'writer', 
            'content', 
            'post', 
            'created_at'
            ]

# 댓글 업데이트
class CommentUpdateModel(BaseCommentModel):
    class Meta(BaseCommentModel.Meta):
        fields = ['content']

# 댓글 삭제
class CommentDeleteModel(BaseCommentModel):
    class Meta(BaseCommentModel.Meta):
        pass
    

