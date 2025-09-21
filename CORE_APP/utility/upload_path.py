def upload_to_pdf(instance, filename):
    return f"uploads/pdfs/{filename}"

def upload_to_img(instance, filename):
    return f"uploads/img/{filename}"

def upload_to_video(instance, filename):
    return f"uploads/video/{filename}"

def upload_to_audio(instance, filename):
    return f"uploads/audio/{filename}"