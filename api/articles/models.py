from django.contrib.auth.models import User
from django.db import models

from authors.models import Author
from common.models import AbstractBaseModel


class Topic(AbstractBaseModel):
    """
    Model for the topics that we are interested in i.e. psychiatry, therapy, data science
    and machine learning.
    Note:- The initial list of topics are loaded via a fixture (./articles/fixtures/topics.json)
    """

    name = models.CharField(max_length=50)

    @property
    def articles_count(self):
        return self.topic_articles.count()


class Article(AbstractBaseModel):
    reference_id = models.CharField(max_length=50, unique=True)
    published = models.DateTimeField()
    title = models.CharField(max_length=255)
    summary = models.TextField()
    authors = models.ManyToManyField(Author, related_name="articles")
    topic = models.ForeignKey(
        Topic, on_delete=models.PROTECT, related_name="topic_articles"
    )
    favorited_users = models.ManyToManyField(User)

    class Meta:
        ordering = ("-published",)

    @property
    def favorited_count(self):
        return self.favorited_users.count()
