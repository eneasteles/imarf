# Generated by Django 3.2.4 on 2023-02-02 14:31

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('chapa', '0011_chapa_pedido'),
        ('comercial', '0014_alter_venda_chapa_produzida_chapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda_chapa_produzida',
            name='chapa',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='bloco', chained_model_field='bloco', on_delete=django.db.models.deletion.PROTECT, to='chapa.chapa'),
        ),
    ]
