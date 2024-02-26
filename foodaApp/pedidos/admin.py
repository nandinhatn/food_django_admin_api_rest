from django.contrib import admin
from .models import Pedidos, ItemPedido
# Register your models here.


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidosAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]

admin.site.register(Pedidos, PedidosAdmin)  # Registrando o modelo PedidosAdmin, não ItemPedido

