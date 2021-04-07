import json

from django.test import LiveServerTestCase, Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from articles.models import Article, Topic


class TestAuthenticationAPI(LiveServerTestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_registration_and_successful_authentication(self):
        username = "admin"
        email = "admin@domain.com"
        password = "doekowkri03i#$J7gh"

        # Register user
        registration_response = self.client.post(
            reverse("registration"),
            {"username": username, "email": email, "password": password},
        )

        self.assertEqual(registration_response.status_code, status.HTTP_200_OK)

        # login
        login_response = self.client.post(
            reverse("token_login"),
            {"username": username, "password": password},
        )

        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        token = json.loads(login_response.content).get("access")

        # access secured resource
        article = Article.objects.create(
            reference_id="w09qwd9iepdpokd",
            title="My Article",
            summary="Article Summary",
            published=timezone.now(),
            topic=Topic.objects.create(name="My Topic"),
        )

        self.client.defaults["HTTP_AUTHORIZATION"] = "Bearer " + token

        favorite_response = self.client.post(
            reverse("favourite_article"),
            {"article": article.pk},
        )

        self.assertEqual(favorite_response.status_code, status.HTTP_200_OK)
