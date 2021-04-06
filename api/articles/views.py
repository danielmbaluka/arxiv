from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.models import Article, Topic
from articles.serialiser import ArticleSerializer, TopicSerializer


class ArticlesView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["topic"]


class ArticlesDetailsView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TopicsView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class FavoriteArticleView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            article = Article.objects.get(pk=request.data.get("article"))
            exists = False
            for user in article.favorited_users.all():
                if user.id == request.user.id:
                    exists = True

            if exists:
                article.favorited_users.remove(request.user)
            else:
                article.favorited_users.add(request.user)
        except Article.DoesNotExist:
            pass
        return Response()
