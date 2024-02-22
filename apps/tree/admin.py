from django.contrib import admin

from . import models


class TreeAdmin(admin.ModelAdmin):
    list_display = ("name", "scientific_name")


# Register your models here.
admin.site.register(models.Tree, TreeAdmin)


class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ("tree", "age", "user", "account", "location", "planted_at")
    list_filter = ("account", "age")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(models.PlantedTree, PlantedTreeAdmin)
admin.site.register(models.Location)
