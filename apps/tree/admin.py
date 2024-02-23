from django.contrib import admin
from unfold.admin import ModelAdmin

from . import models


@admin.register(models.Tree)
class TreeAdmin(ModelAdmin):
    list_display = ("name", "scientific_name")


@admin.register(models.PlantedTree)
class PlantedTreeAdmin(ModelAdmin):
    list_display = ("tree", "age", "user", "account", "location", "planted_at")
    list_filter = ("account", "age")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(models.Location)
class LocationAdmin(ModelAdmin):
    pass
