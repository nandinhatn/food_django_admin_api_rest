from django.contrib import admin

# Register your models here.
from .models import Faixas

class FaixasAdmin(admin.ModelAdmin):
    list_display = ('name', 'value','distance')
    

admin.site.register(Faixas, FaixasAdmin)  # Registra a classe ProductAdmin para o modelo Product no admin