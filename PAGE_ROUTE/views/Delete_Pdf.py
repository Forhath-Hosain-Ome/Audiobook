from django.shortcuts import render

def DeletePdf(request):
    return render (request,'pages/pdf_page/delete_pdf.html')