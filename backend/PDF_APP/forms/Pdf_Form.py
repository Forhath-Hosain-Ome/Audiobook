from django import forms
from PDF_APP.models import PdfModel

class PdfForm(forms.ModelForm):
    class Meta:
        model = PdfModel
        fields = '__all__'
        exclude = ['extracted_text', 'audio_file', 'video_file']