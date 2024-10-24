# Generated by Django 3.2.4 on 2023-02-15 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almoxarifado', '0003_categoria_almoxarifado_classe_almoxarifado_grupo_almoxarifado'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_de_almoxarifado',
            name='categoria',
            field=models.ForeignKey(default='EPI', on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.categoria_almoxarifado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_de_almoxarifado',
            name='classe',
            field=models.ForeignKey(default='MÁSCARA', on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.classe_almoxarifado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item_de_almoxarifado',
            name='grupo',
            field=models.ForeignKey(default='EPI - EQUIPAMENTO DE PROTEÇÃO INDIVIDUAL', on_delete=django.db.models.deletion.CASCADE, to='almoxarifado.grupo_almoxarifado'),
            preserve_default=False,
        ),
    ]
