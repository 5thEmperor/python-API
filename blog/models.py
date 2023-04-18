from django.db import models
from accounts.models import *

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Useraccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title

# class Like(models.Model):
#     user_id= models.ForeignKey(Useraccount,on_delete=models.CASCADE)
#     blog_id= models.ForeignKey(Blog,on_delete=models.CASCADE)
