from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from api.v2.client.serializers import ProfileSerializer, EventInfoSerializer, EventCreateSerializer, InterestSerializer
from rest_framework.response import Response



# class ProfileAPIView(RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     pagination_class = None
#     permission_classes = [AllowAny]


