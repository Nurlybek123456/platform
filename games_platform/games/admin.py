from django.contrib import admin

from .models import Category, Game, GameRating


class CategoryAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    pass

class GameRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameRating, GameRatingAdmin)
