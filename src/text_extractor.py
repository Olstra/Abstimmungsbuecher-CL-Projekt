import fitz


def extract_text(path: str) -> str:
    result = ""

    doc = fitz.open(path)

    for page in doc:
        result += page.get_text("text")

    return result
