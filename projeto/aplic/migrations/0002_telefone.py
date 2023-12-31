# Generated by Django 4.2.5 on 2023-10-04 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11, verbose_name='Número')),
                ('telefone_fornecedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.fornecedor')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
    ]
