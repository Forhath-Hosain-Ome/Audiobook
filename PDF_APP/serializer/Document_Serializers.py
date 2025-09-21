from rest_framework import serializers
from reader.models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'pdf', 'extracted_text', 'audio_file']
        read_only_fields = ['extracted_text', 'audio_file']
