from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from api.v2.client.permissions import IsAdminPermission
from api.v2.client.serializers import PatientSerializer, PatientCreateSerializer
from core.models import Patient


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
