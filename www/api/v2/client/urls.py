from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v2.client.views import PatientsListAPIView, PatientsCreateAPIView, ProfileAPIView, DoctorInfoAPIView, \
    PatientInfoAPIView, DoctorsListAPIView, DoctorsCreateAPIView, AppointmentsListAPIView, AppointmentsCreateAPIView, DepartmentsListAPIView, SpecializationsListAPIView

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('patients/<int:pk>', PatientInfoAPIView.as_view(), name='patients'),
    path('patients', PatientsListAPIView.as_view(), name='patients'),
    path('patients/create', PatientsCreateAPIView.as_view(), name='patients'),
    path('profile', ProfileAPIView.as_view(), name='profile'),
    path('doctors/<int:pk>', DoctorInfoAPIView.as_view(), name='doctors'),
    path('doctors', DoctorsListAPIView.as_view(), name='doctors'),
    path('doctors/create', DoctorsCreateAPIView.as_view(), name='doctors'),
    path('appointments', AppointmentsListAPIView.as_view(), name='appointments'),
    path('appointments/create', AppointmentsCreateAPIView.as_view(), name='appointments'),
    path('departments', DepartmentsListAPIView.as_view(), name='departments'),
    path('specializations', SpecializationsListAPIView.as_view(), name='specializations'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
