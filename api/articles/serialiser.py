from rest_framework import serializers

from articles.models import Article, Topic
from authors.serialiser import AuthorSerializer


class ArticleSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Article
        fields = ("id", "reference_id", "published", "title", "summary", "authors", "favorited_count")


class TopicSerializer(serializers.ModelSerializer):
    articles_count = serializers.ReadOnlyField()

    class Meta:
        model = Topic
        fields = ("id", "name", "articles_count")
