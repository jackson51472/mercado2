# Generated by Django 4.2.5 on 2023-10-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0016_alter_pedido_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[(True, 'Feito'), (False, 'Finalizado')], default=True),
        ),
    ]
