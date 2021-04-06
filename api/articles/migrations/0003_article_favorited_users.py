# Generated by Django 3.1.7 on 2021-04-06 16:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_auto_20210406_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='favorited_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
