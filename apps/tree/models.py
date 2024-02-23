from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    latitude = models.DecimalField(
        _("Latitude"),
        max_digits=10,
        decimal_places=6,
        default=Decimal("0.000000"),
    )
    longitude = models.DecimalField(
        _("Longitude"),
        max_digits=10,
        decimal_places=6,
        default=Decimal("0.000000"),
    )

    def __str__(self) -> str:
        return f"{self.latitude}, {self.longitude}"


class Tree(models.Model):
    class Meta:
        verbose_name = _("Tree")
        verbose_name_plural = _("Trees")

    name = models.CharField(_("Name"), max_length=100)
    scientific_name = models.CharField(_("Scientific Name"), max_length=100)

    def __str__(self) -> str:
        return f"{self.name} - {self.scientific_name}"


class PlantedTree(models.Model):
    class Meta:
        verbose_name = _("Planted tree")
        verbose_name_plural = _("Planted trees")

    age = models.IntegerField(_("Age"))
    planted_at = models.DateTimeField(
        _("Planted At"), auto_now=False, auto_now_add=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )
    tree = models.ForeignKey(
        "tree.Tree",
        verbose_name=_("Tree"),
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        "user.Account",
        verbose_name=_("Account"),
        on_delete=models.CASCADE,
    )

    location = models.ForeignKey(
        "tree.Location", verbose_name=_("Location"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.tree)
