from typing import Optional

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None  # Optional dependency

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

supported_methods = ["pymupdf", "pypdf"]


class PDFReader:
    def __init__(self, method: str = "pypdf"):
        if method not in supported_methods:
            raise ValueError(f"Method must be one of: {supported_methods}")
        if method == "pymupdf" and not fitz:
            raise ImportError("PyMuPDF is not installed")
        if method == "pypdf" and not PdfReader:
            raise ImportError("pypdf is not installed")
        self.method = method

    def extract_text(self, path: str) -> str:
        if self.method == "pymupdf":
            return self._extract_text_pymupdf(path)
        elif self.method == "pypdf":
            return self._extract_text_pypdf(path)

    def _extract_text_pymupdf(self, path: str) -> str:
        return "".join(page.get_text("text") for page in fitz.open(path))

    def _extract_text_pypdf(self, path: str) -> str:
        reader = PdfReader(path)
        result = ""

        for page in reader.pages:
            result += page.extract_text()

        return result
