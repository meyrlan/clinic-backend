import logging

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from drf_spectacular.utils import extend_schema_field
from drf_extra_fields.fields import Base64ImageField
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError

from core.models import Patient, User, Doctor

logger = logging.getLogger(__name__)


class PatientInfoSerializer(serializers.ModelSerializer):
    registration_date = serializers.DateField(read_only=True)
    phone = PhoneNumberField(source="user.phone")
    birth_date = serializers.DateField(source="user.birth_date")

    class Meta:
        model = Patient
        fields = (
            "id",
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


class PatientCreateSerializer(serializers.ModelSerializer):
    registration_date = serializers.DateField(read_only=True)
    phone = PhoneNumberField(write_only=True)
    birth_date = serializers.DateField(write_only=True)
    password = serializers.CharField(write_only=True)

    @transaction.atomic
    def create(self, validated_data):
        phone = validated_data.pop("phone")
        password = validated_data.pop("password")
        birth_date = validated_data.pop("birth_date")

        user = User.objects.filter(phone=phone).first()
        if user:
            raise ValidationError({"error": f"User with phone {phone} already exists."})

        user = User.objects.create_user(
            phone=phone,
            password=password,
            birth_date=birth_date,
        )
        patient = Patient.objects.create(**validated_data)
        patient.user = user
        patient.save()

        return patient

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
            "password",
        )


class DoctorCreateSerializer(serializers.ModelSerializer):
    registration_date = serializers.DateField(read_only=True)
    phone = PhoneNumberField(write_only=True)
    birth_date = serializers.DateField(write_only=True)
    password = serializers.CharField(write_only=True)

    @transaction.atomic
    def create(self, validated_data):
        phone = validated_data.pop("phone")
        password = validated_data.pop("password")
        birth_date = validated_data.pop("birth_date")

        user = User.objects.filter(phone=phone).first()
        if user:
            raise ValidationError({"error": f"User with phone {phone} already exists."})

        user = User.objects.create_user(
            phone=phone,
            password=password,
            birth_date=birth_date,
        )
        doctor = Doctor.objects.create(**validated_data)
        doctor.user = user
        doctor.save()

        return doctor

    class Meta:
        model = Doctor
        fields = (
            "id",
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
            "registration_date",
            "phone",
            "birth_date",
            "password",
        )


class ProfileInfoSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    surname = serializers.SerializerMethodField()
    middle_name = serializers.SerializerMethodField()

    def get_name(self):
        if self.doctor:
            return self.doctor.name
        elif self.admin:
            return self.admin.name
        elif self.patient:
            return self.patient.name
        return None

    def get_surname(self):
        if self.doctor:
            return self.doctor.surname
        elif self.admin:
            return self.admin.surname
        elif self.patient:
            return self.patient.surname
        return None

    def get_middle_name(self):
        if self.doctor:
            return self.doctor.middle_name
        elif self.admin:
            return self.admin.middle_name
        elif self.patient:
            return self.patient.middle_name
        return None

    class Meta:
        model = User
        fields = ("id", "phone", "birth_date", "role", "name", "surname", "middle_name")


class DoctorInfoSerializer(serializers.ModelSerializer):
    registration_date = serializers.DateField(read_only=True)
    phone = PhoneNumberField(source="user.phone")
    birth_date = serializers.DateField(source="user.birth_date")

    class Meta:
        model = Doctor
        fields = (
            "id",
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
            "registration_date",
            "phone",
            "birth_date",
        )
