from rest_framework import serializers
from .models import News, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'category',
        ]




class NewsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'category',
        ]