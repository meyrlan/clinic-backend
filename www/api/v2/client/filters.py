from django_filters import rest_framework as filters
from core.models import Doctor


class DoctorFilter(filters.FilterSet):
    department_id = filters.NumberFilter()

    class Meta:
        model = Doctor
        fields = ("department_id", )
