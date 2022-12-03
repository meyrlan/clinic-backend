from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from api.v2.client.permissions import IsAdminPermission
from api.v2.client.serializers import PatientSerializer, PatientCreateSerializer, ProfileInfoSerializer
from core.models import Patient, User


class PatientsListAPIView(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = None


class PatientInfoAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = None


class PatientsCreateAPIView(CreateAPIView):
    http_method_names = ("post", )
    permission_classes = (AllowAny, )
    serializer_class = PatientCreateSerializer


class ProfileAPIView(RetrieveAPIView):
    http_method_names = ("get", )
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = ProfileInfoSerializer
    pagination_class = None

    def get_object(self):
        return self.request.user
