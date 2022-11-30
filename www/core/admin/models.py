from django.contrib import admin
from core.models import (User, Patient, Doctor, Admin)
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse
from django.utils.html import format_html


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "birth_date")
    search_fields = ("id", "phone")
    fields = ("phone", "birth_date")


@admin.register(Patient)
class PatientModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname", "email")
    readonly_fields = ("registration_date", )
    search_fields = ("id", "iin_number", "id_number", "user", "name", "surname", "email")
    fields = (
        "user",
        "iin_number",
        "name",
        "surname",
        "middle_name",
        "blood_group",
        "emergency_contact_number",
        "email",
        "address",
        "marital_status",
        "registration_date",
    )


@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname")
    search_fields = ("id", "iin_number", "id_number", "name", "surname", "address")
    fields = (
        "user",
        "iin_number",
        "id_number",
        "name",
        "surname",
        "middle_name",
        "department_id",
        "specialization_details_id",
        "experience_years",
        "photo",
        "category",
        "price_per_appointment",
        "schedule_details",
        "degree",
        "rating",
        "address",
        "homepage_url",
    )


@admin.register(Admin)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname")
    search_fields = ("id", "name", "surname")
    fields = (
        "user",
        "name",
        "surname",
        "middle_name",
    )
