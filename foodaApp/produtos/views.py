

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import CustomProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



# class UserList(generics.ListAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

class ProductList(APIView):
    def get(self, request, format=None):
        produtos = Product.objects.all()
        serializer = CustomProductSerializer(produtos, many=True)
        return Response(serializer.data)