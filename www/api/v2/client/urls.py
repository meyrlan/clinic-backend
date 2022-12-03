from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v2.client.views import PatientsListAPIView, PatientInfoAPIView, PatientsCreateAPIView

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('patients', PatientsListAPIView.as_view(), name='patients'),
    path('patients/<int:pk>', PatientInfoAPIView.as_view(), name='patients'),
    path('patients/create', PatientsCreateAPIView.as_view(), name='patients'),
    # path('profile', ProfileAPIView.as_view(), name='profile'),  # Information about user -> role, name, surname
    # path('doctors', DoctorsListAPIView.as_view(), name='doctors'),
    # path('doctors/<int:pk>', DoctorInfoAPIView.as_view(), name='doctor'),
    # path('doctors/<int:pk>', DoctorUpdateAPIView.as_view(), name='doctor'),
    # path('doctors/create', DoctorsCreateAPIView.as_view(), name='doctors'),
    # path('doctors/delete', DoctorsDeleteAPIView.as_view(), name='doctors'),
    # path('departments', DepartmentsListAPIView.as_view(), name='departments'),
    # path('appointments', AppointmentsListAPIView.as_view(), name='appointments'),
    # path('appointments/create', AppointmentCreateAPIView.as_view(), name='appointments'),  # Only patients can create
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
