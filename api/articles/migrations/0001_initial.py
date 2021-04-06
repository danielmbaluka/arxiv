# Generated by Django 3.1.7 on 2021-04-06 11:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("reference_id", models.CharField(max_length=50, unique=True)),
                ("published", models.DateTimeField()),
                ("title", models.CharField(max_length=255)),
                ("summary", models.TextField()),
                (
                    "authors",
                    models.ManyToManyField(
                        related_name="articles", to="authors.Author"
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="articles.topic"
                    ),
                ),
            ],
            options={
                "ordering": ("-published",),
            },
        ),
    ]