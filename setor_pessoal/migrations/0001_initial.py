# Generated by Django 3.2.4 on 2024-12-09 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=15, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_alteracao', models.DateTimeField(auto_now=True)),
                ('centro_de_custo', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='producao.centro_de_custo')),
            ],
        ),
    ]