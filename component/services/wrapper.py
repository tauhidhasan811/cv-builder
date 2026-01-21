import os
from .file_reader import extract_docx, extract_pdf_text


def extract_document(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        #text, _ = extract_pdf_text_and_images(file_path)
        text= extract_pdf_text(file_path)

    elif ext == ".docx":
        text = extract_docx(file_path=file_path)

    else:
        text = f"Unsupported file type: {ext}"

    return text
