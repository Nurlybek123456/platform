from rest_framework import serializers

from users.models import CustomUser

from .choices import rating_choices
from .models import Category, Game, GameRating


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        max_length=100,
        allow_null=False,
        allow_blank=True,
    )
    icon = serializers.CharField(
        required=True,
        max_length=35,
        allow_null=True,
        allow_blank=True,
    )

    class Meta:
        model = Category
        exclude = (
            'created_at',
            'updated_at',
            'deleted_at'
        )


class GameSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=255,
        allow_null=False,
        allow_blank=False,
    )
    description = serializers.CharField(
        max_length=1000,
        allow_null=True,
        allow_blank=True,
    )
    cover = serializers.FileField(
        allow_null=True,
    )
    views = serializers.IntegerField(
        required=False,
        read_only=True,
        allow_null=True,
    )
    category = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=Category.objects.filter(deleted_at=None),
    )

    class Meta:
        model = Game
        exclude = (
            'created_at',
            'updated_at',
            'deleted_at'
        )


class GameRatingSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=Game.objects.filter(deleted_at=None),
    )
    user = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=CustomUser.objects.filter(deleted_at=None),
    )
    value = serializers.ChoiceField(
        required=False,
        choices=rating_choices,
    )


    class Meta:
        model = GameRating
        exclude = (
            'created_at',
            'updated_at',
            'deleted_at'
        )