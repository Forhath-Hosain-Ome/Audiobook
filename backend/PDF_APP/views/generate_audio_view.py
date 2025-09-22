from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from PDF_APP.models import PdfModel
from tasks import generate_audio_task

def Generate_Audio_View(request, pk):
    doc = get_object_or_404(PdfModel, pk=pk)
    generate_audio_task.delay(doc.id)
    return JsonResponse({"message": "Audio generation started!"})