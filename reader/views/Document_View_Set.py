from rest_framework import viewsets, status
from rest_framework.response import Response
from reader.models import DocumentModel
from reader.Serializer import DocumentSerializer
from reader.utils import extract_text_from_pdf
from reader.utils import generate_tts_gtts
from django.conf import settings
from django.core.files import File
import os

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = DocumentModel.objects.all().order_by('-uploaded_at')
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        doc = serializer.save()

        try:
            # 1️⃣ Extract text
            text = extract_text(doc.pdf.path)
            doc.extracted_text = text
            doc.save(update_fields=['extracted_text'])

            # 2️⃣ Generate TTS audio
            audio_filename = os.path.splitext(os.path.basename(doc.pdf.name))[0] + ".mp3"
            audio_dir = os.path.join(settings.MEDIA_ROOT, "uploads", "audio")
            os.makedirs(audio_dir, exist_ok=True)
            audio_path = os.path.join(audio_dir, audio_filename)

            generate_tts_gtts(text, audio_path, lang="bn")

            # Save audio to model
            with open(audio_path, "rb") as f:
                doc.audio_file.save(audio_filename, File(f), save=True)

        except Exception as e:
            doc.delete()  # Remove incomplete document
            raise serializers.ValidationError({"error": f"Failed to process PDF: {e}"})

    def perform_update(self, serializer):
        doc = serializer.save()

        if 'pdf' in self.request.FILES:
            try:
                text = extract_text(doc.pdf.path)
                doc.extracted_text = text
                doc.save(update_fields=['extracted_text'])

                audio_filename = os.path.splitext(os.path.basename(doc.pdf.name))[0] + ".mp3"
                audio_dir = os.path.join(settings.MEDIA_ROOT, "uploads", "audio")
                os.makedirs(audio_dir, exist_ok=True)
                audio_path = os.path.join(audio_dir, audio_filename)

                generate_tts_gtts(text, audio_path, lang="bn")

                with open(audio_path, "rb") as f:
                    doc.audio_file.save(audio_filename, File(f), save=True)

            except Exception as e:
                raise serializers.ValidationError({"error": f"Failed to process PDF: {e}"})
