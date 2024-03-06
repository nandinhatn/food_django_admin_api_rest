from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PedidoSeralizer
from .models import Pedidos, ItemPedido
from produtos.models import Product
from faixas.models import Faixas
import requests

import mercadopago
sdk = mercadopago.SDK("TEST-5315486789325091-112712-af352b2c03deb2097e57d2c7c368ea36-85022863")
class NovoPedido(APIView):
    def post(self, request, format=None):
        serializer = PedidoSeralizer(data=request.data)
        if serializer.is_valid():
            pedido = serializer.save()  # Cria o pedido usando o serializer

            # Processa os itens do pedido
            produtos = request.data.get('produtos', [])  # Lista de produtos pedidos
            faixa_id  = request.data.get('faixa')
            faixa = Faixas.objects.get(id=faixa_id)
            for produto_info in produtos:
                produto_id = produto_info.get('id')
                quantidade = produto_info.get('quantidade')
                produto = Product.objects.get(id=produto_id)
                ItemPedido.objects.create(
                    pedido=pedido,
                    produto=produto,
                    quantidade=quantidade,
                    
                )
            payment_data = {
    "transaction_amount": 100,
    "token": 'ff8080814c11e237014c1ff593b57b4d',
    
    "payer": {
        
        "email": "contato@teste.com",
    },
     "payment_method_id": "pix",
}

          
            request_options = mercadopago.config.RequestOptions()
            payment_response = sdk.payment().create(payment_data, request_options)
            payment = payment_response["response"]
            request_options.custom_headers = {
            'x-idempotency-key': '1234564878'
            }
            response_data ={
                "pedido" : serializer.data,
                "pagamento": payment
                
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MercadoPagoTokenView(APIView):
    def post(self, request):
        
       return Response({"teste" : "teste"})
    def get(self, request):

        payment_methods_response = sdk.payment_methods().list_all()
        payment_methods = payment_methods_response["response"]
        return Response({'resp': payment_methods})