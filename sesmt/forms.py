from django import forms
from .models import PDFDocument

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title','worker', 'enterprise', 'pdf_file']
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'worker': forms.Select(attrs={'class': 'form-control'}),
            'enterprise': forms.Select(attrs={'class': 'form-control'}),
            'pdf_file': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        
