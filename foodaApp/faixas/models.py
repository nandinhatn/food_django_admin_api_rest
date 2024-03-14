from django.db import models

# Create your models here.
class Faixas(models.Model):
    distance = models.IntegerField(verbose_name= 'distância')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor')
    name = models.CharField(default="Faixa Nomear", max_length=20, verbose_name='nome')
    

    class Meta():
        verbose_name_plural= "Faixa"

    def __str__(self):
        return self.name
