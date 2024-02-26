from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PedidoSeralizer
from .models import Pedidos, ItemPedido
from produtos.models import Product

class NovoPedido(APIView):
    def post(self, request, format=None):
        serializer = PedidoSeralizer(data=request.data)
        if serializer.is_valid():
            pedido = serializer.save()  # Cria o pedido usando o serializer

            # Processa os itens do pedido
            produtos = request.data.get('produtos', [])  # Lista de produtos pedidos
            for produto_info in produtos:
                produto_id = produto_info.get('id')
                quantidade = produto_info.get('quantidade')
                produto = Product.objects.get(id=produto_id)
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=produto,
                    quantidade=quantidade
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
