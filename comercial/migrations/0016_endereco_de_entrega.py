# Generated by Django 3.2.4 on 2023-02-28 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0015_alter_venda_chapa_produzida_chapa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco_de_Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.TextField(blank=True, max_length=200, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comercial.pedido_de_venda')),
            ],
        ),
    ]