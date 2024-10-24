# Generated by Django 3.2.4 on 2023-01-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapa', '0007_lancamento_manual_chapa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapa',
            name='espessura',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='chapa',
            name='valor_m2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='lancamento_manual_chapa',
            name='espessura',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
