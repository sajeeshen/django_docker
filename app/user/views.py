from django.shortcuts import render
from django.contrib.auth import get_user_model
from core.models import Profile
from rest_framework import ( viewsets, generics,
                            authentication, permissions)
from .serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.
User = get_user_model()


class UserCreateViewSet(generics.CreateAPIView):
    """ API endpoint that allows to create new user """

    def get_serializer_class(self):
        """ Check the version and return the serializers """
        # if self.request.version == 'v1':
        #     return UserSerializer
        return UserSerializer

class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for users """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Manage the authenticated user """
    
    serializer_class = UserSerializer
    authentication_class = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """ Retrieve and return the user objects """
        return self.request.user
