# Generated by Django 4.1.13 on 2024-02-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_pedidos_forma_pagamento_pedidos_status_pagamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='status_pagamento',
            field=models.CharField(choices=[('PR', 'Processando'), ('AP', 'Pagamento Aprovado'), ('RE', 'Pagamento Recusado')], default='PR', max_length=2),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='status_pedido',
            field=models.CharField(choices=[('RE', 'Recebido'), ('PR', 'Em Produção'), ('SE', ' Saiu para entrega'), ('EN', 'Entrega Realizada')], default='RE', max_length=2),
        ),
    ]
