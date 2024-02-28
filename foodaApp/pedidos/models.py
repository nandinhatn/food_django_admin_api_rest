from django.db import models
from produtos.models import Product

# Create your models here.
class Pedidos (models.Model):
    RECEBIDO = 'RE'
    PRODUCAO ='PR'
    SAIDA_ENTREGA='SE'
    ENTREGUE = 'EN'

    PROCESSANDO = 'PR'
    APROVADO = 'AP'
    RECUSADO = 'RE'

    PIX = 'PIX'
    CARTAO = 'CARD'
    PAG_ENTREGA = 'ENT'


    STATUS_PAGAMENTO_CHOICE =[(PROCESSANDO, 'Processando'), (APROVADO, 'Pagamento Aprovado'), (RECUSADO, 'Pagamento Recusado')]

    TIPO_PAGAMENTO_CHOICE =[(PIX, 'Pix'), (CARTAO,'Cartão'), (PAG_ENTREGA, 'Pagamento na Entrega')]
    

    STATUS__PEDIDO_CHOICE = [ (RECEBIDO, 'Recebido'), (PRODUCAO, 'Em Produção'), (SAIDA_ENTREGA, ' Saiu para entrega'), (ENTREGUE, 'Entrega Realizada')]
    name_client = models.CharField(max_length=20)
    data_pedido= models.DateField(auto_now_add=True)
    observacoes= models.TextField(blank=True)
    address_client= models.TextField()
    cpf_client= models.CharField(max_length=11)
    status_pedido = models.CharField(max_length=2,
                                     choices= STATUS__PEDIDO_CHOICE,
                                     default=RECEBIDO)
    status_pagamento= models.CharField(max_length=2, choices=STATUS_PAGAMENTO_CHOICE, default=PROCESSANDO)
    forma_pagamento = models.CharField(max_length=4, choices = TIPO_PAGAMENTO_CHOICE, default=PAG_ENTREGA )



    def calcular_total(self):
       total = 0
       itens_pedidos = self.itempedido_set.all()
       for item in itens_pedidos:
           total += item.produto.preco * item.quantidade
           print(total)
       return total
   
    
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    produto = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total = {self.produto.preco * self.quantidade}
        print(self.produto.preco)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.produto.preco * self.quantidade}'

   
