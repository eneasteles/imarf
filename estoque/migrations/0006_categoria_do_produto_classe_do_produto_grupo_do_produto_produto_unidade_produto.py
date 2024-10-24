# Generated by Django 3.2.4 on 2023-02-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_remove_estoque_qualidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_do_Produto',
            fields=[
                ('categoria_do_produto', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classe_do_Produto',
            fields=[
                ('classe_do_produto', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_do_Produto',
            fields=[
                ('grupo_do_item', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade_Produto',
            fields=[
                ('unidade', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('fator', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=150)),
                ('apelido', models.CharField(blank=True, max_length=150, null=True)),
                ('inativo', models.BooleanField(default=False)),
                ('valor', models.FloatField(default=0)),
                ('saldo', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categoria_produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.categoria_do_produto')),
                ('classe_produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.classe_do_produto')),
                ('grupo_produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.grupo_do_produto')),
                ('unidade_produto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='estoque.unidade_produto')),
            ],
        ),
    ]
