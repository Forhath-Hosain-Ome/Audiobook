from PDF_APP.models import PdfModel
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from PDF_APP.serializer import DocumentSerializer
import os
from django.conf import settings
from django.core.files import File
from CORE_APP.utility import 

class DocumentDetails(RetrieveUpdateDestroyAPIView):
    queryset = PdfModel.objects.all()
    serializer_class = DocumentSerializer

    def perform_update(self, serializer):
        doc = serializer.save()

        if 'pdf' in self.request.FILES:
            try:
                # Extract text from PDF
                text = extract_text_from_pdf(doc.pdf.path)
                doc.extracted_text = text
                doc.save(update_fields=['extracted_text'])

                # Generate TTS audio
                audio_filename = os.path.splitext(os.path.basename(doc.pdf.name))[0] + ".mp3"
                audio_dir = os.path.join(settings.MEDIA_ROOT, "uploads", "audio")
                os.makedirs(audio_dir, exist_ok=True)
                audio_path = os.path.join(audio_dir, audio_filename)

                generate_tts_gtts(text, audio_path, lang="bn")

                # Attach audio to model
                with open(audio_path, "rb") as f:
                    doc.audio_file.save(audio_filename, File(f), save=True)

            except Exception as e:
                raise serializers.ValidationError({"error": f"Failed to process PDF: {e}"})