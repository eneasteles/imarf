# Generated by Django 3.2.4 on 2024-11-19 13:17

from django.db import migrations, models
import django.db.models.deletion
import sesmt.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setor_pessoal', '__first__'),
        ('cadastro', '0002_alter_adm_empresa_im'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
            ],
        ),
        migrations.CreateModel(
            name='PDFDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('pdf_file', models.FileField(upload_to='pdfs/', validators=[sesmt.validator.validate_pdf], verbose_name='Arquivo PDF')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.adm_empresa', verbose_name='Empresa')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setor_pessoal.cadastro_funcionario', verbose_name='Funcionário')),
            ],
        ),
    ]
