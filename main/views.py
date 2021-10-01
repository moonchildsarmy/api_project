from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerializer, CategorySerializer, NewsCreateSerializer
from .models import News, Category


class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(category=self.request.category)


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


    def perform_create(self, serializer):
        serializer.save(category=self.request.Category)


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsCreateSerializer
    queryset = News.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# Create your views here.
