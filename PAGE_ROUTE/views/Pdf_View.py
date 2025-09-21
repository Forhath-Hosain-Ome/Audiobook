from django.shortcuts import render

def PdfView(request):
    return render (request,'pages/index.html')