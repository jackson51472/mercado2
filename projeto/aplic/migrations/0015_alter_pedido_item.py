# Generated by Django 4.2.5 on 2023-10-02 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0014_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.fornecedor'),
        ),
    ]