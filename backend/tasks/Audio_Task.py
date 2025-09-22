import os
import gtts
from tasks import shared_task
from django.conf import settings
from PDF_APP.models import PdfModel

@shared_task
def generate_audio_task(doc_id):
    doc = PdfModel.objects.get(id=doc_id)

    if not doc.text:
        return "No text found to generate audio!"

    audio_filename = f"{os.path.splitext(os.path.basename(doc.file.name))[0]}.mp3"
    audio_path = os.path.join(settings.MEDIA_ROOT, "audio", audio_filename)
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    engine = gtts.init()
    engine.save_to_file(doc.text, audio_path)
    engine.runAndWait()

    doc.audio.name = f"audio/{audio_filename}"
    doc.save()
    return f"Audio generated for {doc.title}"
