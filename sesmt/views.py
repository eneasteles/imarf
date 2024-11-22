from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFDocument
def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/upload/')  # Redirect to a success page
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})


def pdf_list(request):
    print(request.GET)
    search_query = request.GET.get('q', '')  # Get the search term from the query string
    if search_query.lower() == 'todos':  # Check if the query is 'todos'
        results = PDFDocument.objects.all()
    elif search_query:  # If there's a specific search query
        results = PDFDocument.objects.filter(worker__nome__icontains=search_query)
    else:  # Default case: show the first 5 results
        results = PDFDocument.objects.all()[:10]
    

    return render(request, 'pdf_list.html', {'results': results, 'search_query': search_query})


