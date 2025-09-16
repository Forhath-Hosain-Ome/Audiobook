from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a text-based PDF using pdfminer.six
    """
    text = extract_text(pdf_path)
    # Basic cleanup: strip extra whitespace
    return text.strip()