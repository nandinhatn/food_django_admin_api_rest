from rest_framework import serializers
from .models import Pedidos


class PedidoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields= '__all__'