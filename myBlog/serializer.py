from .models import Post, Comment
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# 기본 설정
class BlogBaseModel(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        # exclude = ['field_to_exclude']
        # 나중에 제외하고 싶은 필드 추가할 때 사용
        
# 게시글 작성
class PostCreateModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        exclude = ['modified_at', 'view_counter',]

# 게시글 상세보기
class PostDetailModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):

        fields = [
            'title', 
            'content',
            'writer',
            'created_at', 
            'modified_at',
            'image',
            'view_count', 
            ]

# 게시글 업데이트
class PostUpdateModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        fields = ['title', 'content', 'image',]

# 게시글 삭제
class PostDeleteModel(BlogBaseModel):
    class Meta(BlogBaseModel.Meta):
        pass

