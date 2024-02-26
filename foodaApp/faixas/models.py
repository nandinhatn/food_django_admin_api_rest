from django.db import models

# Create your models here.
class Faixas(models.Model):
    distance = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name