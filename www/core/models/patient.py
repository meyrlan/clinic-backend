from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    class MARITAL_STATUS(models.TextChoices):
        MARRIED = "married", _("Married")
        SINGLE = "single", _("Single")
        DIVORCED = "divorced", _("Divorced")

    user = models.OneToOneField(
        "core.User",
        verbose_name=_("User"),
        on_delete=models.PROTECT,
        related_name="patient",
        null=True,
        blank=True,
    )

    iin_number = models.CharField(_("IIN Number"), max_length=12)
    id_number = models.CharField(_("ID Number"), max_length=20)
    name = models.CharField(_("Name"), max_length=128)
    surname = models.CharField(_("Surname"), max_length=128)
    middle_name = models.CharField(_("Middle Name"), max_length=128, blank=True)
    blood_group = models.PositiveSmallIntegerField(_("Blood Group"), validators=[MaxValueValidator(4), MinValueValidator(1)])
    emergency_contact_number = PhoneNumberField(_("Emergency Contact Number"), region="KZ")
    email = models.EmailField(_("Email Address"), unique=True, max_length=256, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=256)
    marital_status = models.CharField(_("Marital Status"), max_length=126, choices=MARITAL_STATUS.choices, default=MARITAL_STATUS.SINGLE)
    registration_date = models.DateField(_("Registration Date"), auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name} {self.surname}"

    class Meta:
        db_table = "patients"
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")
