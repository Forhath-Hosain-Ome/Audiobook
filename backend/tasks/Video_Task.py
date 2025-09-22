import os
from tasks import shared_task
from django.conf import settings
from PDF_APP.models import PdfModel
from moviepy.editor import ImageClip, AudioFileClip

@shared_task
def generate_video_from_image_and_audio(document_id):
    try:
        doc = PdfModel.objects.get(id=document_id)

        if not doc.audio_file or not doc.image_file:
            return f"Missing audio or image for Document {document_id}"

        audio_path = os.path.join(settings.MEDIA_ROOT, str(doc.audio_file))
        image_path = os.path.join(settings.MEDIA_ROOT, str(doc.image_file))

        audio = AudioFileClip(audio_path)

        image_clip = ImageClip(image_path).set_duration(audio.duration)

        video_clip = image_clip.set_audio(audio)

        output_path = os.path.join(settings.MEDIA_ROOT, "videos", f"video_{document_id}.mp4")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        video_clip.write_videofile(output_path, fps=24)

        doc.video_file.name = os.path.relpath(output_path, settings.MEDIA_ROOT)
        doc.save()

        return f"Video generated successfully for Document {document_id}"

    except Exception as e:
        return f"Error generating video: {str(e)}"