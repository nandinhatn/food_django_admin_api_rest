# Generated by Django 4.1.13 on 2024-02-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0003_rename_imagem_restaurante_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='end_time',
            field=models.TimeField(default='0:00'),
        ),
        migrations.AddField(
            model_name='restaurante',
            name='start_hours',
            field=models.TimeField(default='0:00'),
        ),
    ]