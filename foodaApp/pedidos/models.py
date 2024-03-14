from django.db import models
from produtos.models import Product
from faixas.models import Faixas


# Create your models here.
class Pedidos (models.Model):
    RECEBIDO = 'RE'
    PRODUCAO ='PR'
    SAIDA_ENTREGA='SE'
    ENTREGUE = 'EN'

    PROCESSANDO = 'PR'
    APROVADO = 'AP'
    RECUSADO = 'RE'

    PIX = 'pix'
    CARTAO = 'credit_card'
    PAG_ENTREGA = 'ENT'


    STATUS_PAGAMENTO_CHOICE =[(PROCESSANDO, 'Processando'), (APROVADO, 'Pagamento Aprovado'), (RECUSADO, 'Pagamento Recusado')]

    TIPO_PAGAMENTO_CHOICE =[(PIX, 'PIX'), (CARTAO,'Cartão'), (PAG_ENTREGA, 'Pagamento na Entrega')]
    

    STATUS__PEDIDO_CHOICE = [ (RECEBIDO, 'Recebido'), (PRODUCAO, 'Em Produção'), (SAIDA_ENTREGA, ' Saiu para entrega'), (ENTREGUE, 'Entrega Realizada')]
    name_client = models.CharField(max_length=20, verbose_name="Nome do Cliente")
    data_pedido= models.DateField(auto_now_add=True)
    observacoes= models.TextField(blank=True, verbose_name= "Observações")
    email_client = models.EmailField(blank=True, default="email@email.com.br", verbose_name= "Email do Cliente")
    address_client= models.TextField(verbose_name="Endereço do Cliente")
    cpf_client= models.CharField(max_length=11, verbose_name='CPF')
    status_pedido = models.CharField(max_length=2,
                                     choices= STATUS__PEDIDO_CHOICE,
                                     default=RECEBIDO)
    status_pagamento= models.CharField(max_length=2, choices=STATUS_PAGAMENTO_CHOICE, default=PROCESSANDO)
    forma_pagamento = models.CharField(max_length=15, choices = TIPO_PAGAMENTO_CHOICE, default=PAG_ENTREGA )

    faixa = models.ForeignKey(Faixas, on_delete=models.CASCADE, default=None, null=True, verbose_name="Frete Faixa")  # Adicionando chave estrangeira para a classe Faixas



    def calcular_total(self):
       total = 0
       itens_pedidos = self.itempedido_set.all()
       for item in itens_pedidos:
           total += item.produto.preco * item.quantidade
           print(total)
       return total
    
    def __str__(self):
         return f'{self.name_client}'
    
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    produto = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantidade = models.PositiveBigIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    
   

    def save(self, *args, **kwargs):

        total_produto = self.produto.preco * self.quantidade
        # if self.faixa:
        #     total_faixa = self.faixa.value
        #     self.total = total_produto 
        
        # else: 
        self.total = total_produto
        
       
     
        

      
        super().save(*args, **kwargs)
    
    class Meta():
        verbose_name_plural  = 'Pedido'
        verbose_name='Pedido'
    def __str__(self):
        return f'{self.produto.name}'


 