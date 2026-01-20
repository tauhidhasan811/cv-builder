import os
import fitz
from docx import Document



def extract_docx(file_path):

    document = Document(file_path)
    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def extract_pdf_text(pdf_path: str):
    doc = fitz.open(pdf_path)

    extracted_text = ""
    for page_index, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            extracted_text += f"\n--- Page {page_index + 1} ---\n{text}"

    return extracted_text
