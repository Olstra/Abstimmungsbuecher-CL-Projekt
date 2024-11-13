import re


class Preprocessor:
    ignored_words = [
        'ja', 'nein', 'enthaltung', 'enthaltungen',
        'oui', 'non', 'abstentions', 'abstention',
        'sì', 'no', 'astensioni', 'astensione',
        'gea', 'na', 'abstenziuns', 'abstenziun'
    ]
    text: str

    def preprocess(self, text) -> str:
        self.text = text
        self.remove_whitespace()
        self.remove_links()
        self.remove_unwanted_words()
        self.remove_numbers()
        self.remove_non_word_and_non_whitespace_chars()

        return self.text

    def remove_whitespace(self):
        return ' '.join(self.text.split())

    def remove_links(self):
        self.text = re.sub(r'admin\.ch[^\s]*', '', self.text)

    def remove_unwanted_words(self):
        pattern = r'\b(?:' + '|'.join(self.ignored_words) + r')\b'
        self.text = re.sub(pattern, '', self.text, flags=re.IGNORECASE)

    def remove_numbers(self):
        self.text = re.sub(r'[0-9%]+', '', self.text)

    def remove_non_word_and_non_whitespace_chars(self):
        self.text = self.text.replace("\u00AD", "")  # remove soft-hyphen delimiter
        self.text = self.text.replace('\b', '')
    