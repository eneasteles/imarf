# Generated by Django 3.2.4 on 2023-01-24 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0020_alter_resinamento_item_preco'),
        ('chapa', '0009_auto_20230123_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento_chapa_quebrada',
            name='chapa_final',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lancamento_chapa_quebrada',
            name='chapa_inicial',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lancamento_chapa_quebrada',
            name='status_chapa',
            field=models.ForeignKey(default='QUEBRADA', on_delete=django.db.models.deletion.PROTECT, to='producao.status_chapa'),
        ),
    ]