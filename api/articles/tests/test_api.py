import json

from django.contrib.auth.models import User
from django.test import LiveServerTestCase, Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from articles.models import Article, Topic
from authors.models import Author


class TestArticlesAPI(LiveServerTestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.articles = [
            {
                "title": "Title One",
                "summary": "Summary One",
                "reference_id": "AGGSU77yuy",
            },
            {
                "title": "Title Two",
                "summary": "Summary Two",
                "reference_id": "HUHSIJIJO",
            },
            {
                "title": "Title Three",
                "summary": "Summary Three",
                "reference_id": "ihdiwdldwn",
            },
        ]

        self.topic = Topic.objects.create(name="Test Topic")

    def _create_articles(self):
        for article in self.articles:
            Article.objects.create(
                reference_id=article.get("reference_id"),
                title=article.get("title"),
                summary=article.get("summary"),
                published=timezone.now(),
                topic=self.topic,
            )

    def test_retrieving_articles_list(self):
        self._create_articles()

        response = self.client.get(reverse("articles_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertEqual(content.get("count"), 3)

    def test_retrieving_single_article(self):
        self._create_articles()

        article = Article.objects.first()

        # add some authors
        author_1 = Author.objects.create(name="My Author")
        author_2 = Author.objects.create(name="Other Author")

        article.authors.add(author_1)
        article.authors.add(author_2)

        response = self.client.get(
            reverse("article_details", kwargs={"pk": article.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertEqual(content.get("title"), article.title)
        self.assertEqual(content.get("summary"), article.summary)
        self.assertEqual(content.get("reference_id"), article.reference_id)
        self.assertEqual(len(content.get("authors")), 2)

    def test_retrieving_topics_list(self):
        self._create_articles()

        response = self.client.get(reverse("topics_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertEqual(content.get("count"), 1)


class TestFavoritingArticles(LiveServerTestCase):
    def setUp(self) -> None:
        self.client = Client()

        User.objects.create_user(
            username="admin", email="user@domain.com", password="siuqiwjsioqw9990090"
        )

        # obtain auth token
        response = self.client.post(
            reverse("token_login"),
            {"username": "admin", "password": "siuqiwjsioqw9990090"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.token = json.loads(response.content).get("access")

    def test_favoriting_an_article(self):
        article = Article.objects.create(
            reference_id="w09qwd9iepdpokd",
            title="My Article",
            summary="Article Summary",
            published=timezone.now(),
            topic=Topic.objects.create(name="My Topic"),
        )

        self.client.defaults['HTTP_AUTHORIZATION'] = 'Bearer ' + self.token
        response = self.client.post(reverse("favourite_article"), {"article": article.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # call API to confirm article has been starred
        response = self.client.get(
            reverse("article_details", kwargs={"pk": article.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = json.loads(response.content)

        self.assertEqual(content.get("favorited_count"), 1)
