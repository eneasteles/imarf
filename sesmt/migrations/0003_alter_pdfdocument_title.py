# Generated by Django 3.2.4 on 2024-11-19 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sesmt', '0002_rename_titulo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfdocument',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sesmt.title', verbose_name='Título'),
        ),
    ]