from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomUserSerializer

# class UserList(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

class UserList(APIView):
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)