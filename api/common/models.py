from django.db import models
from django.utils import timezone


class AbstractBaseModel(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
