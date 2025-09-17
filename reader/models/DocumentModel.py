from django.db import models
from reader.utils import extract_text_from_pdf, generate_tts_gtts
import os
from django.conf import settings
from django.core.files import File

def upload_to_pdf(instance, filename):
    return f"uploads/pdfs/{filename}"

def upload_to_audio(instance, filename):
    return f"uploads/audio/{filename}"

class Document(models.Model):
    title = models.CharField(max_length=255, blank=True)
    pdf = models.FileField(upload_to=upload_to_pdf)
    extracted_text = models.TextField(blank=True)
    audio_file = models.FileField(upload_to=upload_to_audio, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.pdf.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save the PDF first

        if self.pdf and not self.audio_file:  # only process if no audio yet
            pdf_path = self.pdf.path
            text = extract_text_from_pdf(pdf_path)
            self.extracted_text = text

            audio_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".mp3"
            out_path = os.path.join(settings.MEDIA_ROOT, "uploads", "audio", audio_filename)
            generate_tts_gtts(text, out_path, lang="bn")

            with open(out_path, "rb") as f:
                self.audio_file.save(audio_filename, File(f), save=False)

            super().save(update_fields=["extracted_text", "audio_file"])
