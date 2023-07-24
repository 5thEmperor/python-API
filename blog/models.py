from django.db import models
from accounts.models import *

from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    author = models.ForeignKey(Useraccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title


User = get_user_model()

class Like(models.Model):
    like_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    post = models.ForeignKey('Blog', related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')
