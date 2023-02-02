from django_filters import rest_framework as filters

from .models import Category, Game


class CategoryFilter(filters.FilterSet):
    icon = filters.CharFilter(
        field_name="icon",
        lookup_expr="iexact",
    )
    name = filters.CharFilter(
        field_name="name",
        lookup_expr="iexact",
    )

    class Meta:
        model = Category
        fields = [
            "icon",
            "name",
        ]


class GameFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name="title",
        lookup_expr="iexact",
    )
    description = filters.CharFilter(
        field_name="description",
        lookup_expr="icontains",
    )

    class Meta:
        model = Game
        fields = [
            "title",
            "description",
        ]
