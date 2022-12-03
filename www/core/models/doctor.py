from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit


class Doctor(models.Model):
    user = models.OneToOneField(
        "core.User",
        verbose_name=_("User"),
        on_delete=models.PROTECT,
        related_name="doctor",
        null=True,
        blank=True,
    )

    iin_number = models.CharField(_("IIN Number"), max_length=12)
    id_number = models.CharField(_("ID Number"), max_length=20)
    name = models.CharField(_("Name"), max_length=128)
    surname = models.CharField(_("Surname"), max_length=128)
    middle_name = models.CharField(_("Middle Name"), max_length=128, blank=True)
    department_id = models.PositiveIntegerField(_("Department ID"))
    specialization_details_id = models.PositiveIntegerField(_("Specialization Details ID"))
    experience_years = models.IntegerField(_("Experience Years"))
    photo = ProcessedImageField(
        verbose_name=_("Photo"),
        upload_to="doctors/photos/",
        null=True,
        blank=True,
        format="JPEG",
        options={"quality": 90},
        processors=[
            ResizeToFit(width=1920, height=1200, upscale=False),
        ]
    )
    category = models.CharField(_("Category"), max_length=128)
    price_per_appointment = models.IntegerField(_("Price Per Appointment"))
    schedule_details = models.CharField(_("Schedule Details"), max_length=256)
    degree = models.CharField(_("Degree"), max_length=128)
    rating = models.PositiveSmallIntegerField(_("Rating"), validators=[MaxValueValidator(10), MinValueValidator(0)])
    address = models.CharField(_("Address"), max_length=256)
    homepage_url = models.CharField(_("Homepage URL"), max_length=256, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name} {self.surname}"

    class Meta:
        db_table = "doctors"
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")
