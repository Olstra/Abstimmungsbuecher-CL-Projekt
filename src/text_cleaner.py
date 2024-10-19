import re


def clean_text(text: str) -> str:
    text = re.sub(r'[0-9%]+', '', text)
    return ' '.join(text.split())
