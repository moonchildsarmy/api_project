from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('news_create/', views.NewsCreateView.as_view()),
    path('news/', views.NewsListView.as_view()),
    path('news_detail/<int:pk>/', views.NewsDetailView.as_view()),
    path('category/', views.CategoryListView.as_view()),
    path('create_category/', views.CategoryCreateView.as_view()),
    path('category_detail/<int:pk>', views.CategoryUpdateView.as_view()),
]