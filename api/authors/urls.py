from django.conf.urls import url

from authors.views import AuthorsView, AuthorDetailsView

urlpatterns = [
    url(r"^$", AuthorsView.as_view()),
    url(r"^(?P<pk>\d+)/$", AuthorDetailsView.as_view()),
]
