from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Restaurante(models.Model):
    nome = models.CharField(max_length=20 )
    descricao = models.TextField()
    email = models.EmailField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    logo= models.ImageField(upload_to='static/imagens/', default='default.jpg')
    city = models.CharField(max_length=20, default="Sem cidade inforamada")
    start_hours = models.TimeField(default='0:00')
    end_time = models.TimeField(default='0:00')
    telefone = PhoneNumberField()

    class Meta():
        verbose_name_plural = "Restaurante"

    def __str__(self):
        return f"Latitude : {self.latitude}, Longitude : {self.longitude}. Email: {self.email}, nome :{self.email}, descricao:{self.descricao}"