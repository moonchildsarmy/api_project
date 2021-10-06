from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .serializers import NewsSerializer, CategorySerializer, NewsCreateSerializer, CategoryDetailSerializer, NewsDetailSerializer
from .models import News, Category, Journalist


class NewsListView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(category=self.request.Category)

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     title = self.request.query_params.get('title')
    #     search_params = {'title__iexact': title}
    #     return qs.filter(**search_params)

class NewsDetailView(generics.RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()


class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer


class NewsUpdateView(generics.RetrieveUpdateDestroyAPIView):
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


class CategoryShowView(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'


# Create your views here.
