from django.shortcuts import render
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class GetUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Only admins can view all users


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view lets an authenticated user retrieve or update their own profile.
    The IsAuthenticated permission ensures that only users with valid JWT tokens can access this endpoint.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get_object(self):
    # Returns the currently authenticated user.
        return self.request.user

