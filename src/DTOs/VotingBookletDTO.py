from datetime import date
from dataclasses import dataclass, field
from typing import Optional, List
from src.DTOs import PageDTO


# TODO: fix imports of dataclasses in text_extractor

@dataclass
class VotingBookletDTO:
    pages: Optional[List[PageDTO]] = field(default_factory=list)
    date: Optional[date] = None
