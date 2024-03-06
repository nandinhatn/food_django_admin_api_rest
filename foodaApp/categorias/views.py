from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Category
from .serializers import CategoriaSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category
import requests


class CategoryList(APIView):
    def get(self, request, format=None):
        categorias = Category.objects.all()
        serializer = CategoriaSerializer(categorias, many = True)
        return Response(serializer.data)