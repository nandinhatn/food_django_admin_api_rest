from rest_framework import serializers
from .models import Category

from .models import Category

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    