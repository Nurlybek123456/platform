from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GameRatingViewSet, GameViewSet

router = DefaultRouter()
router.register(
    prefix="games",
    basename="games",
    viewset=GameViewSet
)
router.register(
    prefix="categories",
    basename="categories",
    viewset=CategoryViewSet
)
router.register(
    prefix="game_ratings",
    basename="game_ratings",
    viewset=GameRatingViewSet
)

urlpatterns = router.urls