from CORE_APP.models import *
from django.db import models

class PdfModel(BaseModel):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to=upload_to_pdf)
    pdf_image = models.ImageField(upload_to=upload_to_img)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # if self.file:
        #     try:
        #         text = extract_text(self.file.path)
        #         self.extracted_text = text
        #         super().save(update_fields=['extracted_text'])
        #     except Exception as e:
        #         print(f"Text extraction failed: {e}")
