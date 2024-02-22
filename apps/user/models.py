from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class NewUser(AbstractUser):
    account = models.ManyToManyField(
        "user.Account", verbose_name=_("Account"), blank=True
    )


class Profile(models.Model):
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    about = models.TextField(_("About"))
    joined = models.DateTimeField(_("Joined"), auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return self.about


class Account(models.Model):
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    name = models.CharField(_("Name"), max_length=100)
    created = models.DateTimeField(_("Created at"), auto_now=False, auto_now_add=True)
    active = models.BooleanField(_("Active"), default=True)

    def __str__(self) -> str:
        return self.name
