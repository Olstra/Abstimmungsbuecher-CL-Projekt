import unittest

from src.sentence_splitter import split_into_sentences
from src.swissbert.extract_to_json import extract_to_json
from src.swissbert.sentences_aligner import align_sentences
from src.text_cleaner import clean_text
from src.text_extractor import extract_text


class MyTestCase(unittest.TestCase):
    def test_align_de_and_rm(self):
        # DE
        de_test_path = "../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_DE_web.pdf"
        de_text = extract_text(de_test_path)
        de_cleaned_text = clean_text(de_text)
        de_sentences = split_into_sentences(de_cleaned_text)

        # RM
        rm_test_path = "../../../test_data/one_pagers/Seite_5-Erlaeuterungen_Juni_RM_web.pdf"
        rm_text = extract_text(rm_test_path)
        rm_cleaned_text = clean_text(rm_text)
        rm_sentences = split_into_sentences(rm_cleaned_text)

        result = align_sentences(rm_sentences, de_sentences)

        extract_to_json(result)


if __name__ == '__main__':
    unittest.main()
