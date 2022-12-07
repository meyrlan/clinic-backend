from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api.v2.client.permissions import IsAdminPermission
from api.v2.client.serializers import PatientInfoSerializer, PatientCreateSerializer, ProfileInfoSerializer, \
    DoctorInfoSerializer, DoctorCreateSerializer, AppointmentInfoSerializer, AppointmentCreateSerializer, DepartmentInfoSerializer, SpecializationInfoSerializer
from core.models import Patient, User, Doctor, Appointment, Department, Specialization
from api.v2.client.filters import DoctorFilter


class PatientInfoAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Patient.objects.all()
    serializer_class = PatientInfoSerializer
    pagination_class = None


class PatientsListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Patient.objects.all()
    serializer_class = PatientInfoSerializer
    pagination_class = None


class PatientsCreateAPIView(CreateAPIView):
    permission_classes = (IsAdminPermission, )
    serializer_class = PatientCreateSerializer


class ProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = ProfileInfoSerializer
    pagination_class = None

    def get_object(self):
        return self.request.user


class DoctorInfoAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Doctor.objects.all()
    serializer_class = DoctorInfoSerializer
    pagination_class = None


class DoctorsListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Doctor.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_class = DoctorFilter
    serializer_class = DoctorInfoSerializer
    pagination_class = None


class DoctorsCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DoctorCreateSerializer


class AppointmentsListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Appointment.objects.all()
    serializer_class = AppointmentInfoSerializer
    pagination_class = None


class AppointmentsCreateAPIView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AppointmentCreateSerializer


class DepartmentsListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Department.objects.all()
    serializer_class = DepartmentInfoSerializer
    pagination_class = None


class SpecializationsListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Specialization.objects.all()
    serializer_class = SpecializationInfoSerializer
    pagination_class = None
