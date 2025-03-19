from pypdf import PdfReader

from src.nlp.text_cleaner import clean_up_line_breaks


def extract_text_from_pdf(path: str) -> str:
    text = ''.join(page.extract_text() for page in PdfReader(path).pages)
    text = clean_up_line_breaks(text.split('\n'))
    text = '\n'.join(sentence for sentence in text)
    return text