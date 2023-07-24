from rest_framework import serializers
# from .models import Blog, Category, Tag
from . models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']



class BlogSerializer(serializers.ModelSerializer):
    # category= CategorySerializer(many=True, read_only= True)
    class Meta:
        model = Blog
        fields= "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('like_id', 'post', 'user', 'created_at')
# class BlogGetSerializer(serializers.ModelSerializer):
#     categoryname= CategorySerializer(many=True, read_only= True)
#     tagname=TagSerializer(many=True, read_only= True)
#     class Meta:
#         model = Blog
#         fields = ['id' ,'title','category','tags','author','created_at','updated_at','is_published','is_public','status','categoryname','tagname']