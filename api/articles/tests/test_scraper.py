import os
from unittest.mock import patch, MagicMock

from django.test import LiveServerTestCase, Client

from articles.models import Topic, Article
from articles.scraper import Scraper


class TestAPIScraper(LiveServerTestCase):
    def setUp(self) -> None:
        self.client = Client()

    @patch("urllib.request.urlopen")
    def test_scraping(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.getcode.return_value = 200

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )

        with open(os.path.join(__location__, "sample_response.xml")) as f:
            mock_response.read.return_value = f.read()

        mock_urlopen.return_value = mock_response

        topic = Topic.objects.create(name="Test Topic")

        scraper = Scraper()

        scraper.scrape(topic)

        # assert that articles were scraped successfully and added to the database
        articles = Article.objects.all()

        self.assertEqual(len(articles), 2)

        self.assertEqual(articles[0].authors.count(), 6)
        self.assertEqual(articles[1].authors.count(), 2)
