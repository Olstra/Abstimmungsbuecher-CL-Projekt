import re
from typing import List

import fitz
import nltk


class Parser:

    original_text: str
    sentences: List[str]

    def __init__(self):
        pass

    def extract_text_from_pdf(self, path: str) -> "Parser":
        self.original_text = "".join(page.get_text("text") for page in fitz.open(path))
        return self

    def clean_text(self) -> "Parser":
        self.original_text = re.sub(r'[0-9%]+', '', self.original_text)

        # TODO: does this really improve output quality?

        # remove "Yes", "No" for all 4 languages
        self.original_text = re.sub('Ja', '', self.original_text)
        self.original_text = re.sub('Nein', '', self.original_text)
        self.original_text = re.sub('Oui', '', self.original_text)
        self.original_text = re.sub('Non', '', self.original_text)
        self.original_text = re.sub('Sì', '', self.original_text)
        self.original_text = re.sub('No', '', self.original_text)
        self.original_text = re.sub('Na', '', self.original_text)
        self.original_text = re.sub('Gea', '', self.original_text)

        # remove links
        self.original_text = re.sub(r'\b(?:https?://|www\.)\S+|\S+\.(?:ch|com|org|net)\b', '', self.original_text)

        self.original_text = ' '.join(self.original_text.split())

        return self

    def split_into_sentences(self) -> list[str]:
        # TODO: put links into separate elements?
        self.sentences = nltk.sent_tokenize(self.original_text)
        return self.sentences
