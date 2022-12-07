from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(_("Name"), max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "departments"
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")
