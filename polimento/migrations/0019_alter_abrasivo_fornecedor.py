# Generated by Django 3.2.4 on 2023-02-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0021_resinamento_chapa_bloco'),
        ('polimento', '0018_polimento_qualidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abrasivo',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='producao.pessoa'),
        ),
    ]