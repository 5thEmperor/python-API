from django.urls import path
from .views import BlogList, BlogDetail, CategoryList, TagList

urlpatterns = [
    path('blogs/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('tags/', TagList.as_view()),
]


