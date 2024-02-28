from django.contrib import admin
from .models import Pedidos, ItemPedido
from django.utils.html import format_html
# Register your models here.


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


class PedidosAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display=('id','get_custom_name', 'data_pedido','color_status_pedido', 'color_status_pagamento', 'total_pedido')
    
    def get_custom_name(self,obj):
        return obj.name_client
    get_custom_name.short_description='Nome Cliente'

    def color_status_pagamento(self, obj):
        if obj.status_pagamento =='AP':
            color='green'
        elif obj.status_pagamento=='RE':
            color='red'
        else:
            color=''
         
        return format_html('<span style="color: {}; " >{}</span>', color, obj.get_status_pagamento_display())

    color_status_pagamento.short_description ="Status Pagamento"
    color_status_pagamento.allow_tags = True

    def color_status_pedido(self,obj):
        if obj.status_pedido=='PR':
            color='red'
        elif obj.status_pedido=='EN':
            color='green'
        elif obj.status_pedido=='SE':
            color='orange'
        else:
            color=''
        
        return format_html('<span style="color:{}; ">{}</span>', color,obj.get_status_pedido_display())
    color_status_pedido.short_description="Status Pedido"
    color_status_pedido.allow_tags=True

    def total_pedido(self,obj):
        itens_pedido= obj.itempedido_set.all()
        total = sum(item.produto.preco * item.quantidade for item in itens_pedido)
        total_formatado = f' R$ {total:.2f}'
        return total_formatado
    total_pedido.short_description = 'Total do Pedido'
    
admin.site.register(Pedidos, PedidosAdmin)  # Registrando o modelo PedidosAdmin, não ItemPedido

