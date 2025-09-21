from CORE_APP.models import BaseModel
from django.db import models
from CORE_APP.utility import upload_to_pdf, upload_to_img, upload_to_audio, upload_to_video

class PdfModel(BaseModel):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=upload_to_pdf)
    pdf_image = models.ImageField(upload_to=upload_to_img, null=True, blank=True)
    extracted_text = models.TextField(null=True, blank=True)
    audio_file = models.FileField(upload_to=upload_to_audio, null=True, blank=True)
    video_file = models.FileField(upload_to=upload_to_video, null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.file:
            try:
                text = extract_text(self.file.path)
                self.extracted_text = text
                super().save(update_fields=['extracted_text'])
            except Exception as e:
                print(f"Text extraction failed: {e}")
