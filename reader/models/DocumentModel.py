from django.db import models

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
