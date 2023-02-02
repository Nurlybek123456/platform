from django.db import models
from django.db.models import Count

from core.models import CommonModel

from .choices import rating_choices


class Category(CommonModel):
    icon = models.CharField(
        verbose_name="icon",
        max_length=35,
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name="name",
        max_length=100,
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Game(CommonModel):
    title = models.CharField(
        verbose_name="title",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="description",
        null=True,
        blank=True,
    )
    cover = models.FileField(
        verbose_name="cover",
        null=True,
        blank=True,
    )
    views = models.BigIntegerField(
        verbose_name="views_count",
        default=0,
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="category",
        null=True,
        on_delete=models.SET_NULL,
        related_name="games",
    )

    @property
    def rating(self, instance, *args, **kwargs) -> int:
        rate_count_dict = GameRating.objects.values('value').annotate(rate_count=Count('value'))
        return rate_count_dict

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "game"
        verbose_name_plural = "games"


class GameRating(CommonModel):
    game = models.ForeignKey(
        'Game',
        related_name="rating",
        on_delete=models.CASCADE,
    )
    user = models.OneToOneField(
        'users.CustomUser',
        related_name="game_rating",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    value = models.SmallIntegerField(
        verbose_name="rating_value",
        choices=rating_choices,
    )

    class Meta:
        verbose_name = "game_rating"
        verbose_name_plural = "games_ratings"
