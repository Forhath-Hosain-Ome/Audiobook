import os
import fitz
import logging

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None

logging.getLogger("pdfminer").setLevel(logging.ERROR)


def is_scanned_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        page = doc[0]
        text = page.get_text()
        return len(text.strip()) == 0
    except Exception:
        return True


def extract_text(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text + "\n"
        if text.strip():
            return text
    except Exception as e:
        print(f"PyMuPDF failed: {e}")

    if pdfplumber:
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text() or ""
                    text += page_text + "\n"
            if text.strip():
                return text
        except Exception as e:
            print(f"pdfplumber failed: {e}")


    if pytesseract and is_scanned_pdf(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                text += pytesseract.image_to_string(img) + "\n"
            return text
        except Exception as e:
            print(f"OCR failed: {e}")


    return ""



if __name__ == "__main__":
    pdf_file = "sample.pdf"
    if os.path.exists(pdf_file):
        extracted_text = extract_text(pdf_file)
        print(extracted_text)
    else:
        print("PDF file not found.")
