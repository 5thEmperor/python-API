from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog, Category, Like
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import *
from rest_framework.generics import get_object_or_404
import uuid
from .service import *

class BlogList(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        user= request.user.id
        data= request.data
        print("this is data -----------",data)
        # print("this is user token -----------",user)
        
        serializer = BlogSerializer(data=request.data)
        data['author']= user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        data = getprofile(serializer.data)
        return Response(data)


class BlogDetail(APIView):
    # ... (existing code)

    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.check_permissions(request)
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    



class LikeBlog(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        user = request.user
        try:
            like = Like.objects.get(post=blog, user=user)
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            Like.objects.create(post=blog, user=user)
            return Response({"message": "Liked successfully."}, status=status.HTTP_201_CREATED)



