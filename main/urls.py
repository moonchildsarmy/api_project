from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('news/', views.NewsListView.as_view()),
    path('news_detail/', views.NewsDetailView.as_view()),
    path('news_create/', views.NewsCreateView.as_view()),
    path('news_update/<int:pk>/', views.NewsUpdateView.as_view()),
    path('category_show/<int:pk>', views.CategoryShowView.as_view()),
    path('category/', views.CategoryListView.as_view()),
    path('create_category/', views.CategoryCreateView.as_view()),
    path('category_update/<int:pk>', views.CategoryUpdateView.as_view()),
]