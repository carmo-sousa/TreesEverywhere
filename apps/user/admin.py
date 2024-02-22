from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin

from .models import Account, NewUser, Profile


@admin.register(NewUser)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ("name", "created", "active")
    list_filter = ("active",)
    list_editable = ("active",)
    search_fields = ("name",)
