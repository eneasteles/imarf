# Generated by Django 3.2.4 on 2021-07-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0007_auto_20210630_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocoitem',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.bloco'),
        ),
        migrations.AlterField(
            model_name='blocoitem',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.produto'),
        ),
        migrations.AlterField(
            model_name='blocoitem',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.unidade'),
        ),
        migrations.AlterField(
            model_name='chapas_produzidas',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.bloco'),
        ),
        migrations.AlterField(
            model_name='entrada_chapa',
            name='acabamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento'),
        ),
        migrations.AlterField(
            model_name='entrada_chapa',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.bloco'),
        ),
        migrations.AlterField(
            model_name='entrada_chapa',
            name='detalhe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.detalhe'),
        ),
        migrations.AlterField(
            model_name='entrada_chapa',
            name='qualidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.qualidade'),
        ),
        migrations.AlterField(
            model_name='entrada_ladrilho',
            name='acabamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento'),
        ),
        migrations.AlterField(
            model_name='entrada_ladrilho',
            name='detalhe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.detalhe'),
        ),
        migrations.AlterField(
            model_name='entrada_ladrilho',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.material'),
        ),
        migrations.AlterField(
            model_name='entrada_ladrilho',
            name='qualidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.qualidade'),
        ),
        migrations.AlterField(
            model_name='estoque_chapa',
            name='acabamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento'),
        ),
        migrations.AlterField(
            model_name='estoque_chapa',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.bloco'),
        ),
        migrations.AlterField(
            model_name='estoque_chapa',
            name='detalhe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.detalhe'),
        ),
        migrations.AlterField(
            model_name='estoque_chapa',
            name='qualidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.qualidade'),
        ),
        migrations.AlterField(
            model_name='faturamento',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.empresa'),
        ),
        migrations.AlterField(
            model_name='faturamento',
            name='mes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.mes'),
        ),
        migrations.AlterField(
            model_name='fiofatorconversao',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.pessoa'),
        ),
        migrations.AlterField(
            model_name='fiofatorconversao',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.maquina'),
        ),
        migrations.AlterField(
            model_name='folha_de_pagamento',
            name='mes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.mes'),
        ),
        migrations.AlterField(
            model_name='operador',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.setor'),
        ),
        migrations.AlterField(
            model_name='parada',
            name='serrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.serrada'),
        ),
        migrations.AlterField(
            model_name='pedido_venda',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.empresa'),
        ),
        migrations.AlterField(
            model_name='pedido_venda',
            name='forma_pagamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.forma_pagamento'),
        ),
        migrations.AlterField(
            model_name='pedido_venda',
            name='frete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.frete'),
        ),
        migrations.AlterField(
            model_name='pedido_venda',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.pessoa', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='pedido_venda',
            name='status_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.status_venda', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='pedido_venda_item',
            name='acabamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento'),
        ),
        migrations.AlterField(
            model_name='pedido_venda_item',
            name='bloco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.bloco'),
        ),
        migrations.AlterField(
            model_name='pedido_venda_item',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.grupo'),
        ),
        migrations.AlterField(
            model_name='pedido_venda_item',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.material'),
        ),
        migrations.AlterField(
            model_name='pedido_venda_item',
            name='pedido_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.pedido_venda'),
        ),
        migrations.AlterField(
            model_name='pedido_venda_item',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.unidade'),
        ),
        migrations.AlterField(
            model_name='resinamento',
            name='linha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.linha_resinamento'),
        ),
        migrations.AlterField(
            model_name='resinamento',
            name='mes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.mes'),
        ),
        migrations.AlterField(
            model_name='resinamento',
            name='operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.operador'),
        ),
        migrations.AlterField(
            model_name='resinamento_item',
            name='bloco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.bloco'),
        ),
        migrations.AlterField(
            model_name='resinamento_item',
            name='resina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.resina'),
        ),
        migrations.AlterField(
            model_name='resinamento_item',
            name='resinamento_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.resinamento'),
        ),
        migrations.CreateModel(
            name='View_serrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serrada', models.IntegerField()),
                ('data_inicial', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
                ('horimetro_inicial', models.IntegerField()),
                ('horimetro_final', models.IntegerField()),
                ('espessura_fio_inicial', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('espessura_fio_final', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('qtde_fios', models.IntegerField()),
                ('observacoes', models.TextField()),
                ('periferica', models.DecimalField(decimal_places=3, max_digits=5)),
                ('cala', models.IntegerField(default=10)),
                ('consumo_kwh', models.DecimalField(decimal_places=3, default=0, max_digits=7)),
                ('jogo_fio_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.fio_diamantado')),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.maquina')),
            ],
        ),
    ]