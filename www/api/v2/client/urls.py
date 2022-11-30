from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v2.client.views import PatientsListAPIView, PatientInfoAPIView, PatientsCreateAPIView

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('patients', PatientsListAPIView.as_view(), name='patients'),
    path('patients/<int:pk>', PatientInfoAPIView.as_view(), name='patients'),
    path('patients/create', PatientsCreateAPIView.as_view(), name='patients'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
