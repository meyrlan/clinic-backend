from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from api.v2.client.views import (
#     ProfileAPIView,
# )

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    # path("profile/<int:pk>", ProfileAPIView.as_view(), name="profile"),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
