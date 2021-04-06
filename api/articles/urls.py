from django.conf.urls import url

from articles.views import (
    ArticlesView,
    ArticlesDetailsView,
    TopicsView,
    FavoriteArticleView,
)

urlpatterns = [
    url(r"^$", ArticlesView.as_view()),
    url(r"^(?P<pk>\d+)/$", ArticlesDetailsView.as_view()),
    url(r"^topics/$", TopicsView.as_view()),
    url(r"^favorite/$", FavoriteArticleView.as_view()),
]
