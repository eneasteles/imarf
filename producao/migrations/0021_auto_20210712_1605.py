# Generated by Django 3.2.4 on 2021-07-12 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0020_auto_20210712_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custos_Pedreira',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField(default=2021)),
                ('mes', models.IntegerField(choices=[(1, 'JANEIRO'), (2, 'FEVEREIRO'), (3, 'MARÇO'), (4, 'ABRIL'), (5, 'MAIO'), (6, 'JUNHO'), (7, 'JULHO'), (8, 'AGOSTO'), (9, 'SETEMBRO'), (10, 'OUTUBRO'), (11, 'NOVEMBRO'), (12, 'DEZEMBRO')])),
                ('valor', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('pedreira', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.pedreira')),
            ],
        ),
        migrations.CreateModel(
            name='Producao_Pedreira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m3', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('custos_producao_pedreira_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.custos_pedreira')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.material')),
            ],
        ),
        migrations.DeleteModel(
            name='Custos_Producao',
        ),
    ]