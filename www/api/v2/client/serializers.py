import logging

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from drf_spectacular.utils import extend_schema_field
from drf_extra_fields.fields import Base64ImageField
from django.db import transaction

from core.models import Patient

logger = logging.getLogger(__name__)


class PatientSerializer(serializers.ModelSerializer):
    registration_date = serializers.DateField(read_only=True)
    phone = PhoneNumberField(source="user.phone")
    birth_date = serializers.DateField(source="user.birth_date")

    class Meta:
        model = Patient
        fields = (
            "iin_number",
            "id_number",
            "name",
            "surname",
            "middle_name",
            "blood_group",
            "emergency_contact_number",
            "email",
            "address",
            "marital_status",
            "registration_date",
            "birth_date",
            "phone",
        )
