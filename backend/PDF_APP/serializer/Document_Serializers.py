from rest_framework import serializers
from PDF_APP.models import PdfModel

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfModel
        fields = ['id', 'title', 'pdf', 'extracted_text', 'audio_file']
        read_only_fields = ['extracted_text', 'audio_file']
