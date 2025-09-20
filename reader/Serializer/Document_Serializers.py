from rest_framework import serializers
from reader.models import DocumentModel

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ['id', 'title', 'pdf', 'extracted_text', 'audio_file', 'uploaded_at']
        read_only_fields = ['extracted_text', 'audio_file', 'uploaded_at']
