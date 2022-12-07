from django.db import models
from django.utils.translation import gettext_lazy as _


class Specialization(models.Model):
    name = models.CharField(_("Name"), max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "specializations"
        verbose_name = _("Specialization")
        verbose_name_plural = _("Specializations")
