from django.contrib import admin

from .models import CustomUser  # , UserDetail

admin.site.register(CustomUser)

# class UserDetailAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(UserDetail, UserDetailAdmin)
