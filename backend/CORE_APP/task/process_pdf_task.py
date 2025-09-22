from celery import shared_task
from django.core.files.base import ContentFile
from PDF_APP.models import PdfModel
from CORE_APP.utility import extract_text
import pyttsx3  # or gTTS for cloud voices
import os
from io import BytesIO

@shared_task
def process_pdf(doc_id):
    doc = PdfModel.objects.get(id=doc_id)

    # 1. Extract text
    text = extract_text(doc.file.path)
    doc.extracted_text = text

    # 2. Generate audio (TTS)
    audio_io = BytesIO()
    engine = pyttsx3.init()
    engine.save_to_file(text, "temp_audio.mp3")
    engine.runAndWait()

    # Save audio file in model
    with open("temp_audio.mp3", "rb") as f:
        doc.audio_file.save(f"{doc.id}_audio.mp3", ContentFile(f.read()), save=False)

    os.remove("temp_audio.mp3")

    # Save everything
    doc.save(update_fields=["extracted_text", "audio_file"])
