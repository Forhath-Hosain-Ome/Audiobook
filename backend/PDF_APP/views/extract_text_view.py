from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from PDF_APP.models import PdfModel
from tasks import extract_text_task

def Extract_Text_View(request, pk):
    doc = get_object_or_404(PdfModel, pk=pk)
    extract_text_task.delay(doc.id)
    return JsonResponse({"message": "Text extraction started!"})