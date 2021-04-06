import json

from django.test import Client, LiveServerTestCase
from django.urls import reverse
from rest_framework import status
from django.utils import timezone

from articles.models import Topic, Article
from authors.models import Author


class TestAuthorsAPI(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def test_retrieving_all_authors(self):
        authors = ["Author A", "Author B", "Author C"]
        for name in authors:
            Author.objects.create(name=name)

        response = self.client.get(reverse("authors_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)
        self.assertTrue(content.get("count", 3))
        for author in content.get("results"):
            self.assertIn(author.get("name"), authors)

    def test_retrieving_single_author(self):
        author = Author.objects.create(name="ABC. DE")

        response = self.client.get(reverse("author_details", kwargs={"pk": author.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)

        self.assertEqual(content.get("id"), author.id)
        self.assertEqual(content.get("name"), author.name)

    def test_author_with_articles(self):
        author = Author.objects.create(name="John Doe")
        topic = Topic.objects.create(name="Physics")

        article_1 = Article.objects.create(
            title="My Article",
            summary="Article Summary",
            topic=topic,
            reference_id="66w5hhsausu",
            published=timezone.now(),
        )

        article_2 = Article.objects.create(
            title="Other Article",
            summary="Other Summary",
            topic=topic,
            reference_id="wj1jiiojeojoie",
            published=timezone.now(),
        )

        article_1.authors.add(author)
        article_2.authors.add(author)

        response = self.client.get(reverse("author_details", kwargs={"pk": author.pk}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)

        self.assertEqual(content.get("articles_count"), 2)
