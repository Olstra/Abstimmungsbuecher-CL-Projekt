from dataclasses import dataclass, field
from typing import Optional, List
from datetime import date

import fitz


@dataclass
class PageDTO:
    page_number: Optional[int] = None
    text_content: Optional[str] = None


@dataclass
class VotingBookletDTO:
    pages: Optional[List[PageDTO]] = field(default_factory=list)
    date: Optional[date] = None


def extract_text(path: str) -> VotingBookletDTO:
    result = VotingBookletDTO()

    doc = fitz.open(path)

    for page_nr, page in enumerate(doc, start=1):
        new_page = PageDTO(page_number=page_nr)
        new_page.text_content = page.get_text("text")
        result.pages.append(new_page)

    return result


if __name__ == "__main__":
    test_path = "../../test_data/five_pagers/Erste_5-Erlaeuterungen_Juni_DE_web.pdf"
    extracted_text = extract_text(test_path)
    print(extracted_text.pages)
