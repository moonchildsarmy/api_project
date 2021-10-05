from rest_framework import serializers
from .models import News, Category, Journalist


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField('get_news')

    class Meta:
        model = Category
        fields = ['name', 'news']

    def get_news(self, obj):
        news = News.objects.filter(category=obj)
        return NewsSerializer(news, many=True).data


class JournalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journalist
        fields = ['first_name', 'last_name']


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    journalist = JournalistSerializer()

    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'category',
            'journalist',
        ]


class JournalistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journalist
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    journalist = JournalistDetailSerializer()

    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'category',
            'journalist',
        ]


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'description',
            'category',
            'journalist',
        ]


