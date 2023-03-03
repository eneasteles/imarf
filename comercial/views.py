from django.shortcuts import render

# Create your views here.
import io
from django.http import FileResponse, Http404, HttpResponse
from reportlab.pdfgen import canvas
from .models import *
from django.shortcuts import render, get_object_or_404, redirect

def pedido_pdf(request,id):    
    try:
        obj = Pedido_de_venda.objects.get(pk=id)
        obj_item = Pedido_de_venda_item.objects.filter(pedido_de_venda=id)
        obj_endereco = Endereco_de_Entrega.objects.filter(pedido_de_venda=id)
    except Pedido_de_venda.DoesNotExist:
        raise Http404("Pedido não encontrado")
    return render(request, "comercial/pedido.html", {'pedido': obj, 'pedido_item': obj_item, 'pedido_endereco': obj_endereco,})

def some_view(request, id):
    obj = get_object_or_404(Pedido_de_venda, id=id)
    context = {
        "object": obj
    }
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world."+str(obj.id))

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello2.pdf')
