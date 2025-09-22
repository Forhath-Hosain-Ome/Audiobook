from CORE_APP.models import BaseModel
from django.db import models
from CORE_APP.utility import upload_to_dir
from CORE_APP.utility import extract_text
import os

class PdfModel(BaseModel):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to=upload_to_dir, blank=True, null=True)
    image = models.ImageField(upload_to=upload_to_dir, null=True, blank=True)
    extracted_text = models.TextField(null=True, blank=True)
    extracted_text_file = models.FileField(upload_to=upload_to_dir, null=True, blank=True)
    audio = models.FileField(upload_to=upload_to_dir, null=True, blank=True)
    video = models.FileField(upload_to=upload_to_dir, null=True, blank=True)

    
    def __str__(self):
        return self.title


    # def save(self, *args, **kwargs):
    #     # If the txt file exists, update extracted_text from it
    #     if self.extracted_text_file and self.extracted_text_file.name:
    #         txt_path = self.extracted_text_file.path
    #         if os.path.exists(txt_path):
    #             try:
    #                 with open(txt_path, 'r', encoding='utf-8') as f:
    #                     self.extracted_text = f.read()
    #             except Exception as e:
    #                 print(f"Failed to read extracted text file: {e}")
    #     super().save(*args, **kwargs)

    #     if self.pdf:
    #         try:
    #             text = extract_text(self.pdf.path)
    #             self.extracted_text = text
    #             # Save text to a .txt file in the same directory as the PDF
    #             base, _ = os.path.splitext(os.path.basename(self.pdf.name))
    #             txt_filename = f"{base}.txt"
    #             txt_dir = os.path.dirname(self.pdf.path)
    #             txt_path = os.path.join(txt_dir, txt_filename)
    #             with open(txt_path, 'w', encoding='utf-8') as f:
    #                 f.write(text)
    #             # Store the relative path for FileField
    #             rel_txt_path = os.path.join(os.path.dirname(self.pdf.name), txt_filename)
    #             self.extracted_text_file.name = rel_txt_path
    #             super().save(update_fields=['extracted_text', 'extracted_text_file'])
    #         except Exception as e:
    #             print(f"Text extraction failed: {e}")
