from django.shortcuts import render
from PDF_APP.forms import PdfForm


def AddPdf(request):
    if request.method == "POST":
        addpdf = PdfForm(request.POST, request.FILES)
        if addpdf.is_valid():
            addpdf.save()
    else:
        addpdf = PdfForm()
    return render(request, 'pages/pdf_page/add_pdf.html', {'form': addpdf})