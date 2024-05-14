from rest_framework import serializers
from .models import (Category,
                     Comment,
                     LaveComment,
                     Services,
                     About,
                     Author,
                     Tags,
                     Food,
                     Good,
                     News,
                     OpenHours)

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class OpenHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHours
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class LaveCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaveComment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagsSerializer()
    author = AuthorSerializer()

    class Meta:
        model = Food
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
