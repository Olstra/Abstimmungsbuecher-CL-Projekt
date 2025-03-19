from pypdf import PdfReader


def extract_text_from_pdf(path: str) -> str:
    return ''.join(page.extract_text() for page in PdfReader(path).pages)
