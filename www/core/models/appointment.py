from django.db import models
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    doctor = models.ForeignKey(
        "core.Doctor",
        verbose_name=_("Doctor"),
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    patient = models.ForeignKey(
        "core.Patient",
        verbose_name=_("Patient"),
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    time = models.TimeField(_("Time"))

    def __str__(self):
        return f"{self.id} - {self.patient.name}, {self.doctor.name}"

    class Meta:
        db_table = "appointments"
        verbose_name = _("Appointment")
        verbose_name_plural = _("Appointments")
