# Generated by Django 3.2.4 on 2021-11-11 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '__first__'),
        ('bens', '0002_remove_bem_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='bem',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producao.empresa'),
        ),
    ]
