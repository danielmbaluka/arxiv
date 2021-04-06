from rest_framework import serializers

from articles.models import Article
from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    articles_count = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = ("id", "name", "articles_count")


class AuthorArticlesSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Article
        fields = ("id", "title", "summary", "published", "authors", "favorited_count")


class AuthorDetailsSerializer(serializers.ModelSerializer):
    articles_count = serializers.ReadOnlyField()
    articles = AuthorArticlesSerializer(many=True)

    class Meta:
        model = Author
        fields = ("id", "name", "articles_count", "articles")
