from .models import Post, Comment
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class BlogBaseModel(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        # exclude = ['field_to_exclude']
        # 나중에 제외하고 싶은 필드 추가할 때 사용
        






