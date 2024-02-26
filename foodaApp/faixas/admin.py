from django.contrib import admin

# Register your models here.
from .models import Faixas


admin.site.register(Faixas)  # Registra a classe ProductAdmin para o modelo Product no admin