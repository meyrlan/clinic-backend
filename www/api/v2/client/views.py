from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from api.v2.client.filters import DoctorFilter
from api.v2.client.permissions import IsAdminPermission
from api.v2.client.serializers import PatientInfoSerializer, PatientCreateSerializer, ProfileInfoSerializer, \
    DoctorInfoSerializer, DoctorCreateSerializer
from core.models import Patient, User, Doctor


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
    filter_backends = (DjangoFilterBackend, )
    filter_class = DoctorFilter
    permission_classes = (AllowAny, )
    queryset = Doctor.objects.all()
    serializer_class = DoctorInfoSerializer
    pagination_class = None


class DoctorsCreateAPIView(CreateAPIView):
    permission_classes = (IsAdminPermission, )
    serializer_class = DoctorCreateSerializer
