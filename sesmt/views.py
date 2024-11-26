from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFDocument
from cadastro.models import UserEnterprise


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_pdf')  # Redirect to a success page
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})



def pdf_list(request):
    search_query = request.GET.get('q', '').strip()
    results = PDFDocument.objects.none()  # Inicializa como vazio

    if request.user.is_superuser:
        results = PDFDocument.objects.all()
        print(f"O usuário {request.user} é um superusuário.")
    else:
        try:
            user_enterprises = UserEnterprise.objects.filter(user=request.user).values_list('enterprise', flat=True)
            print(f"Usuário: {request.user}, Empresas Associadas: {list(user_enterprises)}")
            if user_enterprises:
                results = PDFDocument.objects.filter(enterprise__in=user_enterprises)
            else:
                print(f"O usuário {request.user} não está associado a nenhuma empresa.")
        except Exception as e:
            print(f"Erro ao buscar empresas associadas ao usuário {request.user}: {e}")

    if search_query:
        results = results.filter(worker__nome__icontains=search_query)

    print(f"Documentos exibidos para {request.user}: {results}")
    return render(request, 'pdf_list.html', {'results': results, 'search_query': search_query})
