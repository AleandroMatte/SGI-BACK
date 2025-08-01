from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SGAUserModel

@admin.register(SGAUserModel)
class SGAUserAdmin(UserAdmin):
    pass