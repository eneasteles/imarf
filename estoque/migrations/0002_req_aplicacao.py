# Generated by Django 3.2.4 on 2021-12-13 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bens', '0003_bem_empresa'),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='req',
            name='aplicacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='bens.bem'),
            preserve_default=False,
        ),
    ]
