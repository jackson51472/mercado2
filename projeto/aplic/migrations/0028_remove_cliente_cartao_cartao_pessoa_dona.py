# Generated by Django 4.2.5 on 2023-10-03 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0027_alter_itempedido_item_alter_itempedido_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cartao',
        ),
        migrations.AddField(
            model_name='cartao',
            name='pessoa_Dona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.cliente'),
        ),
    ]
