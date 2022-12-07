import logging

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from drf_spectacular.utils import extend_schema_field
from drf_extra_fields.fields import Base64ImageField
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError

from core.models import Patient, User, Doctor, Appointment, Department, Specialization

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
            "specialization",
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
            "department",
            "specialization",
            "password",
        )


class ProfileInfoSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    surname = serializers.SerializerMethodField()
    middle_name = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    def get_name(self, user):
        if hasattr(user, "doctor"):
            return user.doctor.name
        elif hasattr(user, "admin"):
            return user.admin.name
        elif hasattr(user, "patient"):
            return user.patient.name
        return None

    def get_surname(self, user):
        if hasattr(user, "doctor"):
            return user.doctor.surname
        elif hasattr(user, "admin"):
            return user.admin.surname
        elif hasattr(user, "patient"):
            return user.patient.surname
        return None

    def get_middle_name(self, user):
        if hasattr(user, "doctor"):
            return user.doctor.middle_name
        elif hasattr(user, "admin"):
            return user.admin.middle_name
        elif hasattr(user, "patient"):
            return user.patient.middle_name
        return None

    def get_role(self, user):
        return user.role

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
            "specialization",
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


class AppointmentInfoSerializer(serializers.ModelSerializer):
    doctor = DoctorInfoSerializer()
    patient = PatientInfoSerializer()

    class Meta:
        model = Appointment
        fields = (
            "doctor",
            "patient",
            "time",
        )


class AppointmentCreateSerializer(serializers.ModelSerializer):
    doctor_id = serializers.IntegerField(write_only=True)
    patient_id = serializers.IntegerField(write_only=True)

    @transaction.atomic
    def create(self, validated_data):
        doctor_user = User.objects.filter(id=validated_data["doctor_id"]).first()
        patient_user = User.objects.filter(id=validated_data["patient_id"]).first()

        if not hasattr(doctor_user, "doctor"):
            raise ValidationError({"error": f"User with ID {validated_data['doctor_id']} doesn't exist"})
        if not hasattr(patient_user, "patient"):
            raise ValidationError({"error": f"User with ID {validated_data['patient_id']} doesn't exist"})

        validated_data["doctor_id"] = doctor_user.doctor.id
        validated_data["patient_id"] = patient_user.patient.id
        return super().create(validated_data)

    class Meta:
        model = Appointment
        fields = ("doctor_id", "patient_id", "time")


class DepartmentInfoSerializer(serializers.ModelSerializer):
    doctors = DoctorInfoSerializer(many=True)

    class Meta:
        model = Department
        fields = ("id", "name", "doctors")


class SpecializationInfoSerializer(serializers.ModelSerializer):
    doctors = DoctorInfoSerializer(many=True)

    class Meta:
        model = Specialization
        fields = ("id", "name", "doctors")
