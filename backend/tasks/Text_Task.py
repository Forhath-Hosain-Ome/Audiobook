import fitz
from tasks import shared_task
from PDF_APP.models import PdfModel

@shared_task
def extract_text_task(doc_id):
    doc = PdfModel.objects.get(id=doc_id)
    pdf_path = doc.file.path
    text = ""

    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text("text")

    doc.text = text
    doc.save()
    return f"Text extracted for {doc.title}"

