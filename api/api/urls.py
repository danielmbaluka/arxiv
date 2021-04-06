from django.conf.urls import url, include

from articles import urls as articles_urls
from authors import urls as authors_urls
from authentication import urls as authentication_urls


urlpatterns = [
    url(r"^authors/", include(authors_urls)),
    url(r"^articles/", include(articles_urls)),
    url(r"^auth/", include(authentication_urls)),
]
