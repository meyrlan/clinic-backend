from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.v2.client.serializers import PatientSerializer
from core.models import Patient


class PatientsListAPIView(ListAPIView):
    http_method_names = ("get", )
    permission_classes = (AllowAny, )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = None
