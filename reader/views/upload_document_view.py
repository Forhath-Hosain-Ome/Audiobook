from django.shortcuts import render, redirect
from reader.forms import DocumentForm
from reader.utils import extract_text_from_pdf, generate_tts_gtts
from django.conf import settings
import os
from django.core.files import File

def upload_document(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.save()  # save file to get path

            pdf_path = doc.pdf.path
            # 1. Extract text
            text = extract_text_from_pdf(pdf_path)
            doc.extracted_text = text
            doc.save()

            # 2. Generate TTS (gTTS)
            audio_filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".mp3"
            out_path = os.path.join(settings.MEDIA_ROOT, "uploads", "audio", audio_filename)
            generate_tts_gtts(text, out_path, lang="bn")
            # attach audio to model
            with open(out_path, "rb") as f:
                doc.audio_file.save(audio_filename, File(f), save=True)

            return redirect('document_detai', pk=doc.pk)
    else:
        form = DocumentForm()
    return render(request, "reader/upload.html", {"form": form, "errors": form.errors})