# Generated by Django 3.2.4 on 2023-02-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapa', '0011_chapa_pedido'),
        ('polimento', '0019_alter_abrasivo_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapas_ini_fin',
            name='chapa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chapa.chapa'),
        ),
    ]