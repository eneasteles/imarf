from django.db import models
from django.core.exceptions import ValidationError
from .validator import validate_pdf
from setor_pessoal.models import Cadastro_Funcionario
from cadastro.models import Adm_empresa
from datetime import datetime

class Title(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")

    def __str__(self):
        return self.title

class PDFDocument(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name="Título", help_text="Selecione o tipo de documento")  # Optional: A title for the PDF
    worker = models.ForeignKey(Cadastro_Funcionario, on_delete=models.CASCADE, verbose_name="Funcionário",help_text="Selecione o funcionário relacionado ao PDF.")  # Optional: A title for the PDF
    enterprise = models.ForeignKey(Adm_empresa, on_delete=models.CASCADE, verbose_name="Empresa", help_text="Somente arquivo PDF é aceito!")  # Optional: A title for the PDF
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="Arquivo PDF",validators=[validate_pdf])  # Directory where PDFs are saved
    emissao_documento = models.DateField(default=datetime.now, help_text="Data de emissão do documento que se refere ao mês e ano do documento.")
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for uploads

    def __str__(self):
        return str(self.title)
    