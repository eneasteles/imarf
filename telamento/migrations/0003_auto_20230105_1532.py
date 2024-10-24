# Generated by Django 3.2.4 on 2023-01-05 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0015_alter_chapa_unique_together'),
        ('telamento', '0002_telamento_chapa'),
    ]

    operations = [
        migrations.AddField(
            model_name='telamento_chapa',
            name='quantidade_insumo',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='telamento_chapa',
            name='resina',
            field=models.ForeignKey(default=59, on_delete=django.db.models.deletion.PROTECT, to='producao.resina', verbose_name='Tela'),
        ),
        migrations.AddField(
            model_name='telamento_chapa',
            name='unidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='producao.unidade'),
        ),
    ]
