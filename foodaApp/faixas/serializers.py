from rest_framework import serializers

from .models import Faixas


class FaixasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faixas
        fields = '__all__'