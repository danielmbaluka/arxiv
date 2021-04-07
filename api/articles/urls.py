from django.conf.urls import url

from articles.views import (
    ArticlesView,
    ArticlesDetailsView,
    TopicsView,
    FavoriteArticleView,
)

urlpatterns = [
    url(r"^$", ArticlesView.as_view(), name="articles_list"),
    url(r"^(?P<pk>\d+)/$", ArticlesDetailsView.as_view(), name="article_details"),
    url(r"^topics/$", TopicsView.as_view(), name="topics_list"),
    url(r"^favorite/$", FavoriteArticleView.as_view(), name="favourite_article"),
]
