# Generated by Django 3.2.4 on 2023-01-26 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polimento', '0017_alter_polimento_acabamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='polimento',
            name='qualidade',
            field=models.ForeignKey(default='PRIMEIRA', on_delete=django.db.models.deletion.PROTECT, to='polimento.qualidade'),
            preserve_default=False,
        ),
    ]