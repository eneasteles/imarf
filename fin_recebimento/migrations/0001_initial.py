# Generated by Django 3.2.4 on 2023-03-28 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producao', '0024_auto_20230308_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_tipo_documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recebimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_recebido', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('emissao', models.DateField(default=django.utils.timezone.now)),
                ('modo_de_lancamento', models.CharField(choices=[('A', 'Automático'), ('M', 'Manual')], default='M', max_length=1)),
                ('status', models.CharField(choices=[('A', 'Aberto'), ('P', 'Pago'), ('C', 'Cancelado')], default='A', max_length=1)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.empresa')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.pessoa')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_recebimento.fin_tipo_documento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recebimento_vencimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcela', models.IntegerField(default=1)),
                ('vencimento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_recebido', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('emissao', models.DateField(default=django.utils.timezone.now)),
                ('recebimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_recebimento.recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recebimento_comissao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentual', models.DecimalField(decimal_places=2, max_digits=2)),
                ('recebimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_recebimento.recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Forma_de_pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('numero_de_parcelas', models.IntegerField(default=1)),
                ('quantidade_de_dias', models.IntegerField(default=30)),
                ('percentual_da_parcela', models.DecimalField(decimal_places=2, default=0, max_digits=2)),
                ('recebimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fin_recebimento.recebimento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
