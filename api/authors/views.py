from django.db.models import OuterRef, Subquery, Count
from rest_framework.generics import ListAPIView, RetrieveAPIView

from articles.models import Article
from authors.models import Author
from authors.serialiser import AuthorSerializer, AuthorDetailsSerializer


class AuthorsView(ListAPIView):
    queryset = Author.objects.annotate(
        last_publish_date=Subquery(
            Article.objects.filter(authors__pk=OuterRef("pk"))
            .order_by("-published")
            .values("published")[:1]
        ),
        articles_count_=Count("articles"),
    ).order_by("-last_publish_date", "-articles_count_")

    serializer_class = AuthorSerializer


class AuthorDetailsView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailsSerializer
