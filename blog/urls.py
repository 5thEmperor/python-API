from django.urls import path
from .views import BlogList, BlogDetail, CategoryList, TagList


urlpatterns = [
    path('v6/blogs', BlogList.as_view()),
    path('v7/blogs/<int:pk>', BlogDetail.as_view()),
    path('v8/categories', CategoryList.as_view()),
    path('v9/tags', TagList.as_view()),
]


