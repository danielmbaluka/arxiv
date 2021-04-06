from django.db import models

from common.models import AbstractBaseModel


class Author(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)

    @property
    def articles_count(self):
        return self.articles.count()
