from django.shortcuts import render
from .serializers import RestauranteSerializer
from .models import Restaurante
from rest_framework.response import Response

from rest_framework.views import APIView



class RestauranteList(APIView):
    def get(self, request, format=None):
        restaurate = Restaurante.objects.all()
        serializer = RestauranteSerializer(restaurate, many = True)
        return Response()
# Create your views here.
