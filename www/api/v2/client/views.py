from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from api.v2.client.permissions import IsAdminPermission
from api.v2.client.serializers import PatientInfoSerializer, PatientCreateSerializer, ProfileInfoSerializer
from core.models import Patient, User, Doctor


class PatientInfoAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Patient.objects.all()
    serializer_class = PatientInfoSerializer
    pagination_class = None


class PatientsCreateAPIView(CreateAPIView):
    http_method_names = ("post", )
    permission_classes = (IsAdminPermission, )
    serializer_class = PatientCreateSerializer


class ProfileAPIView(RetrieveAPIView):
    http_method_names = ("get", )
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = ProfileInfoSerializer
    pagination_class = None

    def get_object(self):
        return self.request.user


# class DoctorInfoAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView):
#     permission_classes = (AllowAny, )
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorInfoSerializer
#     pagination_class = None
