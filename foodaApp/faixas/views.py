from django.shortcuts import render

from rest_framework import generics
from .models import Faixas
from rest_framework.response import Response
from .serializers import FaixasSerializer
from  rest_framework.views import APIView

# Create your views here.
class FaixasList(APIView):
    def get(self, request, format=None):
            faixas = Faixas.objects.all()
            serializer = FaixasSerializer(faixas, many=True)
            return Response(serializer.data)

