from typing import Tuple

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.response import Response

from .filters import CategoryFilter, GameFilter
from .models import Category, Game, GameRating
from .serializers import (CategorySerializer, GameRatingSerializer,
                          GameSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    http_method_names: Tuple = ("get", "post", "patch", "delete")
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(deleted_at=None)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoryFilter


class GameViewSet(viewsets.ModelViewSet):
    http_method_names: Tuple = ("get", "post", "patch", "delete")
    serializer_class = GameSerializer
    queryset = Game.objects.filter(deleted_at=None)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GameFilter

    def retrieve(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.views += 1
        instance.save()
        return Response(
            data={
                "status": "success",
                "data": serializer.data,
            }
        )

    def list(self, request):
        category = request.GET.get('category', "")
        queryset = Game.objects.all()
        if category:
            queryset = queryset.filter(category=category)
        serializer = GameSerializer(queryset, many=True)
        return Response(data=serializer.data)

class GameRatingViewSet(viewsets.ModelViewSet):
    http_method_names: Tuple = ("get", "post", "patch", "delete")
    serializer_class = GameRatingSerializer
    queryset = GameRating.objects.filter(deleted_at=None)
