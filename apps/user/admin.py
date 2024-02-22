from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account, NewUser, Profile


class CustomUserAdmin(UserAdmin):
    fieldsets = (*UserAdmin.fieldsets, (None, {"fields": ("account",)}))


admin.site.register(NewUser, CustomUserAdmin)
admin.site.register(Profile)


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "active")
    list_filter = ("active",)
    list_editable = ("active",)
    search_fields = ("name",)


admin.site.register(Account, AccountAdmin)
