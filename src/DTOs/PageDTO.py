from dataclasses import dataclass
from typing import Optional


@dataclass
class PageDTO:
    page_number: Optional[int] = None
    text_content: Optional[str] = None
