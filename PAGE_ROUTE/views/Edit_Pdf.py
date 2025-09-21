from django.shortcuts import render

def EditPdf(request):
    return render (request,'pages/pdf_page/edit_pdf.html')