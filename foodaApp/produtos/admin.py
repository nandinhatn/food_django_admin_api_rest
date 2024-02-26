from django.contrib import admin
from django.utils.html import format_html
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_custom_name', 'get_custom_description', 'get_custom_price', 'get_custom_disponibilidade', 'get_custom_meiaporcao', 'display_image')  # Lista de campos a serem exibidos na visualização da lista de produtos

    def get_custom_name(self, obj):
        return obj.name
    get_custom_name.short_description='Nome do Produto'


    def get_custom_description(self, obj):
        return obj.name
    get_custom_description.short_description="Descrição"

    def get_custom_price(self, obj):
        return obj.name
    get_custom_price.short_description = "Preço"

    def get_custom_disponibilidade(self, obj):
        return obj.name
    get_custom_disponibilidade.short_description = "Disponibilidade"

    def get_custom_meiaporcao(self, obj):
        return obj.name
    get_custom_meiaporcao.short_description = "1/2 Porção"

    def display_image(self, obj):
        return  format_html('<img src="{}" width="100" />',obj.imagem.url)  # Retorna a tag HTML para exibir a imagem

    display_image.allow_tags = True  # Permite o uso de tags HTML na coluna
    display_image.short_description = 'Imagem'  # Define o cabeçalho da coluna como 'Imagem'

admin.site.register(Product, ProductAdmin)  # Registra a classe ProductAdmin para o modelo Product no admin