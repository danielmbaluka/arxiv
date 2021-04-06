from celery import shared_task

from articles.models import Topic
from articles.scraper import Scraper


@shared_task(
    name="articles.tasks.scrape_articles", queue="articles.tasks.scrape_articles"
)
def scrape_articles():
    for topic in Topic.objects.all():
        scraper = Scraper()
        scraper.scrape(topic)
