# Generated by Django 3.2.4 on 2024-12-10 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0001_initial'),
        ('polimento', '0004_auto_20241210_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapas_Polidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mudanca_numero', models.BigIntegerField(default=0, verbose_name='Mudança/Set')),
                ('qtde_chapas', models.PositiveIntegerField(default=0)),
                ('chapas_quebradas', models.PositiveIntegerField(default=0)),
                ('velocidade', models.PositiveIntegerField(default=0)),
                ('acabamento', models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento')),
                ('bloco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.bloco')),
            ],
        ),
        migrations.RemoveField(
            model_name='chp_pol_por_jogo_de_abr',
            name='bloco',
        ),
        migrations.RemoveField(
            model_name='chp_pol_por_jogo_de_abr',
            name='jogo_de_abrasivos',
        ),
        migrations.RemoveField(
            model_name='chp_pol_por_jogo_de_abr',
            name='maquina',
        ),
        migrations.RemoveField(
            model_name='chp_pol_por_jogo_de_abr',
            name='tipo_polimento',
        ),
        migrations.RemoveField(
            model_name='consumo_de_abrasivos',
            name='abrasivo',
        ),
        migrations.RemoveField(
            model_name='consumo_de_abrasivos',
            name='unidade',
        ),
        migrations.RemoveField(
            model_name='jogo_de_abrasivos',
            name='abrasivo',
        ),
        migrations.RemoveField(
            model_name='set_de_abrasivos',
            name='maquina',
        ),
        migrations.RemoveField(
            model_name='set_de_abrasivos',
            name='set_de_abrasivos',
        ),
        migrations.AlterField(
            model_name='troca_de_jogo_de_abrasivos',
            name='cabeca',
            field=models.PositiveIntegerField(default=0, verbose_name='Cabeça'),
        ),
        migrations.AlterField(
            model_name='troca_de_jogo_de_abrasivos',
            name='finalizado',
            field=models.BooleanField(default=False, verbose_name='Finalizado'),
        ),
        migrations.AlterField(
            model_name='troca_de_jogo_de_abrasivos',
            name='tipo_de_abrasivo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='polimento.abrasivo', verbose_name='Abrasivo'),
        ),
        migrations.DeleteModel(
            name='Chapas_Ini_Fin',
        ),
        migrations.DeleteModel(
            name='Chp_Pol_por_Jogo_de_Abr',
        ),
        migrations.DeleteModel(
            name='Consumo_de_Abrasivos',
        ),
        migrations.DeleteModel(
            name='Jogo_de_Abrasivos',
        ),
        migrations.DeleteModel(
            name='Set_de_Abrasivos',
        ),
    ]