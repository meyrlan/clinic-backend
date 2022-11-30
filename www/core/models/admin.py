from django.db import models
from django.utils.translation import ugettext_lazy as _


class Admin(models.Model):
    user = models.OneToOneField(
        "core.User",
        verbose_name=_("User"),
        on_delete=models.PROTECT,
        related_name="admin",
        null=True,
        blank=True,
    )

    name = models.CharField(_("Name"), max_length=128)
    surname = models.CharField(_("Surname"), max_length=128)
    middle_name = models.CharField(_("Middle Name"), max_length=128, blank=True)

    class Meta:
        db_table = "admins"
        verbose_name = _("Admin")
        verbose_name_plural = _("Admins")
