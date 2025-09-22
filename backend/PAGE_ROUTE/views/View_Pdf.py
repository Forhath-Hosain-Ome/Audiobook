from django.shortcuts import render
from PDF_APP.models import PdfModel

def ViewPdf(request):
    pdfs = PdfModel.objects.all()
    return render (request,'pages/pdf_page/view_pdf.html', {'pdfs':pdfs})