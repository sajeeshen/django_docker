from django.shortcuts import render
from django.contrib.auth import get_user_model
from core.models import Profile
from rest_framework import viewsets, generics
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.
User = get_user_model()


class UserCreateViewSet(generics.CreateAPIView):
    """ API endpoint that allows to create new user """

    def get_serializer_class(self):
        # if self.request.version == 'v1':
        #     return UserSerializer
        return UserSerializer

class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for users """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
