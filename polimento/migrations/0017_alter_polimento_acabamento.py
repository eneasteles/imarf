# Generated by Django 3.2.4 on 2023-01-26 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0020_alter_resinamento_item_preco'),
        ('polimento', '0016_auto_20230126_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polimento',
            name='acabamento',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento'),
        ),
    ]