from django.contrib import admin
from django.utils.html import format_html
from .models import Restaurante

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'latitude', 'longitude', 'email', 'telefone', 'display_logo')
    def display_logo(self,obj):
        return  format_html('<img src="{}" width="100" />',obj.logo.url)
    display_logo.allow_tags = True  # Permite o uso de tags HTML na coluna
    display_logo.short_description = 'Logo'  # Define o cabeçalho da coluna como 'Imagem'


# Register your models here.
admin.site.register(Restaurante, RestauranteAdmin)  # Registra a classe ProductAdmin para o modelo Product no admin