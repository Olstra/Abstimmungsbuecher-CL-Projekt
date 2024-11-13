from dataclasses import dataclass
from typing import List

from src.common.ch_languages import ch_langs


@dataclass
class CHSentencesLists:
    get: {
        ch_langs.DE: List[str],
        ch_langs.FR: List[str],
        ch_langs.IT: List[str],
        ch_langs.RM: List[str],
    }


if __name__ == "__main__":
    # sample usage
    example = {
        ch_langs.DE: ["List[str]"],
        ch_langs.FR: ["List[str]"],
        ch_langs.IT: ["List[str]"],
        ch_langs.RM: ["List[str]"],
    }
    obj = CHSentencesLists(example)
    print(obj.get['de_CH'])
