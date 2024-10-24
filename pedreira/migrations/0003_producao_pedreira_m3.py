# Generated by Django 3.2.4 on 2023-01-12 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0020_alter_resinamento_item_preco'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedreira', '0002_remove_lancamento_item_leitura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producao_pedreira_m3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=2023)),
                ('mes', models.IntegerField(default=1)),
                ('m3', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.empresa')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.material')),
                ('pedreira', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.pedreira')),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lancamento de Produção',
                'verbose_name_plural': 'Produção',
            },
        ),
    ]
