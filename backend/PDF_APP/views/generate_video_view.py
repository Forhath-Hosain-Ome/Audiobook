from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from PDF_APP.models import PdfModel
from tasks import generate_video_task


def Generate_Video_View(request, pk):
    doc = get_object_or_404(PdfModel, pk=pk)
    image_or_video = request.POST.get("media_file")  # path to image/video
    generate_video_task.delay(doc.id, image_or_video)
    return JsonResponse({"message": "Video generation started!"})
