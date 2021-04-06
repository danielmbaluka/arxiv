import time

from datetime import datetime, timedelta, timezone
from urllib import request, parse
from xml.etree import ElementTree as ET
from urllib.error import HTTPError
from pytz import UTC
from django.conf import settings

from articles.models import Article
from authors.models import Author

ARXIV_SEARCH_BASE = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
OPEN_SEARCH_NS = "{http://a9.com/-/spec/opensearch/1.1/}"

PUBLISHED_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class Scraper(object):
    def scrape(self, topic):
        page = 0
        total_items = 1
        page_size = settings.SCRAPING_PAGE_SIZE

        while (page * page_size) < total_items:
            url = "{base_url}?search_query={search_field}:{topic}&start={start}&max_results={max_results}".format(
                start=page * page_size,
                max_results=page_size,
                base_url=ARXIV_SEARCH_BASE,
                search_field=settings.SCRAPING_SEARCH_FIELD,
                topic=parse.quote(topic.name),
            )

            print("scraping url {}".format(url))

            try:
                response = request.urlopen(url)
                page += 1
            except HTTPError as e:
                if e.code == 503:
                    wait_time = int(e.headers.get("retry-after", 30))
                    print(
                        "Exceeded request rate limit (503). Retrying after {0:d} seconds".format(
                            wait_time
                        )
                    )
                    time.sleep(wait_time)
                    continue
                else:
                    raise e
            xml = response.read()
            root = ET.fromstring(xml)

            entries = root.findall("{}entry".format(ATOM_NS))

            total_items = int(root.find("{}totalResults".format(OPEN_SEARCH_NS)).text)

            for entry in entries:
                self.persist_entry_to_database(entry, topic)

    def persist_entry_to_database(self, entry, topic):
        identifier = self._get_element_text(entry.find("{}id".format(ATOM_NS)))
        date_published_str = self._get_element_text(
            entry.find("{}published".format(ATOM_NS))
        )
        title = self._get_element_text(entry.find("{}title".format(ATOM_NS)))
        summary = self._get_element_text(entry.find("{}summary".format(ATOM_NS)))

        date_published = datetime.strptime(
            date_published_str, PUBLISHED_DATE_FORMAT
        ).replace(tzinfo=UTC)

        # If the article is older than 6 months, ignore it
        now = datetime.now(timezone.utc)
        # bankers definition:- 1 month = 30 days
        if now - date_published > timedelta(days=30 * 6):
            return

        # save the article
        try:
            article = Article.objects.get(reference_id=identifier)
        except Article.DoesNotExist:
            article = Article()
            article.reference_id = identifier
            article.published = date_published
            article.topic = topic

        article.title = title
        article.summary = summary
        article.save()

        # extract and save authors of the article
        authors = entry.findall("{}author".format(ATOM_NS))

        for author_element in authors:
            author_name_element = author_element.find("{}name".format(ATOM_NS))
            author_name = self._get_element_text(author_name_element)

            author, _ = Author.objects.get_or_create(name=author_name)

            # save article authors
            article.authors.add(author)

    def _get_element_text(self, element):
        return element.text.strip().replace("\n", " ")
